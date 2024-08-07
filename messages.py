from db import db
import users
import topics

def get_messages(topic_id):
    sql = """
            SELECT M.id, M.content, M.time sent, U.name 
            FROM messages M, users U 
            WHERE U.id = M.user_id AND M.topic_id = :topic_id
    """
    res = db.session.execute(sql, {"topic_id": topic_id})
    return res.fetchall()

#def send_message(topic_id, content):
    