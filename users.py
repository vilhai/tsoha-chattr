from sqlalchemy import false
from db import db
from sqlalchemy.sql import text
import werkzeug.security
from secrets import token_hex
from flask import session

def logincheck(un, pw):
    sql = text("SELECT id, password, modstatus FROM users WHERE username=:un")
    res = db.session.execute(sql, {"un":un})

    userid = res.fetchone()

    if userid:
        if werkzeug.security.check_password_hash(userid.password, pw):
            session["user_id"] = userid.id
            session["csrf_token"] = token_hex(16)
            session["mod_status"] = 0

            if userid.modstatus:
                session["mod_status"] = userid.id
            
            return True

    return False

def register_user(un, pw):
    pw_hash = werkzeug.security.generate_password_hash(pw)

    sql = text("INSERT INTO users (username, password, modstatus) VALUES (:un, :pw, false)")

    try:
        db.session.execute(sql, {"un":un, "pw":pw_hash})
        db.session.commit()
    except:
        return False
    
    return logincheck(un, pw)


def logout():
    del session["user_id"]
    del session["csrf_token"]
    del session["mod_status"]

def get_userid():
    return session.get("user_id", 0)

def get_mod():
    return session.get("mod_status", 0)