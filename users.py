import db
import werkzeug.security
from flask import session

def logincheck(un, pw):
    sql = """
            SELECT id, password 
            FROM users 
            WHERE username=:un
        """
    res = db.session.execute(sql, {"un":un})

    userid = res.fetchone()

    if userid:
        if werkzeug.security.check_password_hash(userid.password, pw):
            session["user_id"] = userid.id
            return True

    return False

def get_userid():
    return session.get("user_id", 0)