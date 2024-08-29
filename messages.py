from flask import redirect
from db import db
from sqlalchemy.sql import text
import users
import topics

def get_messages(topic_id):
    sql = text("SELECT M.id, M.content, M.time_sent, U.username FROM messages M, users U WHERE U.id = M.user_id AND M.topic_id = :topic_id")
    res = db.session.execute(sql, {"topic_id": topic_id})
    return res.fetchall()

def send_message(topic_id, content):

    if users.get_userid() == 0:
        return False

    sql = text("INSERT INTO messages (topic_id, user_id, content, time_sent) VALUES (:topicid, :userid, :content, NOW())")

    try:
        db.session.execute(sql, {"topicid":topic_id, "userid":users.get_userid(), "content":content})
        db.session.commit()
    except:
        return False
    
    return redirect("/")

def like_message(msg_id):

    if users.get_userid() == 0:
        return False

    sql = text("INSERT INTO likes (user_id, message_id) VALUES (:userid, :msgid)")

    try:
        db.session.execute(sql, {"msgid":msg_id, "userid":users.get_userid()})
        db.session.commit()
    except:
        return False
    
    return redirect("/")

def get_topic_id(msgid):
    sql = text("SELECT topic_id FROM messages WHERE id = :msg_id")
    res = db.session.execute(sql, {"msg_id": msgid})
    return res.fetchone()[0]