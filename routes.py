from app import app
from flask import render_template, request, redirect
from datetime import datetime
from flask import session
import users
import messages
import topics

@app.route("/")
def index():
    topicslist = topics.get_topics()
    return render_template("index.html", topics=topicslist)

@app.route("/topic/<int:topicid>")
def topic(topicid):
    msglist = messages.get_messages(topicid)
    likelist = messages.get_user_likes(topicid)
    like_amounts = {}

    for i in msglist:
        like_amounts[i.id] = len(messages.get_msg_likes(i.id))

    return render_template("topic.html", messages=msglist, topicid=topicid, likes=likelist, like_amounts=like_amounts)

@app.route("/send/<int:topicid>", methods=["GET", "POST"])
def send(topicid):
    if request.method == "POST":
        content = request.form["content"]

        if request.form["csrf_token"] != session["csrf_token"]:
            abort(403)

        if messages.send_message(topicid, content):
            return redirect(f"/topic/{topicid}")
        else:
            return render_template("error.html", msg="Couldn't send the message. Are you signed in?")
        

@app.route("/like/<int:msgid>")
def like(msgid):

    if messages.like_message(msgid):
        return redirect(f"/topic/{messages.get_topic_id(msgid)}")
    else:
        return render_template("error.html", msg="Couldn't like the message. Are you signed in?")

@app.route("/dislike/<int:msgid>")
def dislike(msgid):

    if messages.dislike_message(msgid):
        return redirect(f"/topic/{messages.get_topic_id(msgid)}")
    else:
        return render_template("error.html", msg="Couldn't dislike the message. Are you signed in?")
        
    
    

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        un = request.form["username"]
        pw = request.form["password"]

        if users.logincheck(un, pw):
            return redirect("/")
        else:
            return render_template("error.html", msg="Incorrect username or password")
        
    return render_template("login.html")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        un = request.form["username"]
        pw1 = request.form["password1"]
        pw2 = request.form["password2"]

        if pw1 != pw2:
            return render_template("error.html", msg="The passwords differ. Try again.")

        if users.register_user(un, pw1):
            return redirect("/")
        else:
            return render_template("error.html", msg="Couldn't register. The username might be in use already.")
        
    return render_template("register.html")