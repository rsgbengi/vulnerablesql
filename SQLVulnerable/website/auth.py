from flask import Blueprint
from flask.templating import render_template

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html", text="Testing")


@auth.route("/logout")
def logout():
    return "<p>logout</p>"


@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")