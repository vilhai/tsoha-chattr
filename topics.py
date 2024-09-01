from db import db
from sqlalchemy.sql import text
from flask import redirect
import users
import messages

def get_topics():
    sql = text("SELECT id, name FROM topics")
    res = db.session.execute(sql)
    return res.fetchall()

def get_topic_name(topicid):
    sql = text("SELECT name FROM topics WHERE id = :topicid")
    res = db.session.execute(sql, {"topicid":topicid})
    return res.fetchone()

def create_topic(topicname):
    if users.get_userid() == 0 or users.get_mod() == 0:
        return False

    sql = text("INSERT INTO topics (name) VALUES (:name)")

    try:
        db.session.execute(sql, {"name":topicname})
        db.session.commit()
    except:
        return False
    
    return redirect("/")