from db import db
from sqlalchemy.sql import text
import users
import messages

def get_topics():
    sql = text("SELECT id, name FROM topics")
    res = db.session.execute(sql)
    return res.fetchall()

