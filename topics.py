from db import db
import users
import messages

def get_topics():
    sql = """
            SELECT id, name FROM topics
    """
    res = db.session.execute(sql)
    return res.fetchall()

