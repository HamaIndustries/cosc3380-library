def page_template(body, head="", footer="") -> str:
    return f""" 
    <html>
    <head>
    <style>

    </style>
    {head}
    </head><body>{body}</body>{footer}
    </html>"""

def user_bad_input():
    return page_template("<div>You appear to have input invalid data! Please return to the previous page and try again.</div>")