from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def index():
    return render_template("index.html")

@views.route("/index")
def index2():
    return render_template("index.html")

@views.route("/gendisease")
def gendisease():
    return render_template("gendisease.html")

@views.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

@views.route("/hospital-tracker")
def hospital():
    return render_template("hospital-tracker.html")