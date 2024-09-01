from db import db
from sqlalchemy.sql import text
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