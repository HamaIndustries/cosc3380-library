from base64 import b64encode
from uuid import uuid4
from datetime import datetime, timedelta

from database.connection import get_conn
from web import response, redirect, HTTPRequest
from pages import templates

class ErrorInvalidCredentials(Exception):
    pass

def encrypt(username: str, password: str) -> str:
    # basic string encryption: encrypts password, then salts with username
    crypt = lambda x: b64encode(x.encode('utf-8')).decode('utf-8')
    return crypt(username + "_" + crypt(password))

def validate_user(username, password): # -> (user_id)
    with get_conn().cursor() as curs:
        curs.execute(
            f"select * from library.user where username like %s and password_hash like %s", (username, encrypt(username, password))
        )
        try:
            return curs.fetchall()[0][0]
        except IndexError:
            raise ErrorInvalidCredentials()

def make_session(uid) -> str:
    # creates session for user, returning session cookie value.
    cookie = str(uuid4())[:20]
    conn = get_conn()
    with conn.cursor() as curs:
        curs.execute(
            f"delete from library.session where user_id = %s", (str(uid))
        )

        curs.execute(
            f"insert into library.session (user_id, cookie, expires) values (%s, %s, %s)", 
            (uid, cookie, datetime.now()+timedelta(days=2))
        )
    conn.commit()
    return cookie


def login_page(request: HTTPRequest):
    if request.env['REQUEST_METHOD'] == 'GET':
        body = """
        <form method="post" action="/login" enctype='multipart/form-data'>
            <div>Username: <input type="text" name="username" id="username"></div>
            <div>Password: <input type="password" name="password" id="password"></div>
            <input type="submit" value="Log in">
        </form>
        """
        return response(request, templates.page_template(body))


    elif request.env['REQUEST_METHOD'] == 'POST':
        username = request.data["username"][0]
        password = request.data["password"][0]

        try:
            user = validate_user(username, password)
        except ErrorInvalidCredentials:
            return response(request, templates.user_bad_input())
        
        cookie = make_session(user)
        return redirect(request, "/NavPage", headers={f"Set-Cookie": "libsitecookie=" + cookie})

"""
request has request.session and request.user attributes.

request.session is the session cookie, like 'e702190d-5c78-4ce9-9'
request.user is a dict of user info, like {'first_name': 'elijah', 'last_name': 'mitchell', 'user_type': 'STAFF', 'enabled': True, 'username': 'emitche5'}
"""