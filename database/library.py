from database.connection import get_conn

def user_from_session_token(token: str):
    with get_conn().cursor() as curs:
        curs.execute("""
        select first_name, last_name, utyp.name, enabled, username from
        library.user usr
        left join library.usertype utyp
        on usr.user_type_id = utyp.id
        inner join library.session sess
        on sess.user_id = usr.id
        where sess.cookie like %s
        """, (token,))

        try:
            usr = curs.fetchall()[0]
        except IndexError:
            return None

        return dict(zip(["first_name", 'last_name', 'user_type', 'enabled', 'username'], usr))
    