from app import app
from flask import render_template, request, redirect
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
    return render_template("topics.html", messages=msglist, topic=topicid)

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