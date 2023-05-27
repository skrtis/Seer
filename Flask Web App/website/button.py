from flask import Blueprint, render_template, request

homebut = Blueprint('homebut',__name__)

@homebut.route('/')
def homebutton():
    return render_template("home.html")


