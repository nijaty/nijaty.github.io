from flask import render_template
from models import *


def index_view():
    #template-e melumat buradan
    context = {}
    context["portfolio"] = Portfolio.all()
    return render_template("index.html", **context)