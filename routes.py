from app import app
from flask import render_template, request, redirect
import users
import messages
import topics

@app.route("/")
def index():
    topicslist = topics.get_topics()
    return render_template("index.html", topics=topicslist)

@app.route("topics/<int:topicid>")
def topics(topicid):
    msglist = messages.get_messages(topicid)
    return render_template("topics.html", messages=msglist, topic=topicid)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        un = request.form["username"]
        pw = request.form["password"]

        if users.logincheck(un, pw):
            return redirect("/")
        else:
            return render_template("error.html", message="Incorrect username or password")
        
    render_template(login.html)