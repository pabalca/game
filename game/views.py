from flask import abort, flash, redirect, render_template, session, url_for, request
import random

from game import app
from game.models import Question, db


@app.route("/", methods=["GET", "POST"])
def index():
    q = Question.query.all()
    rand = random.randrange(0, len(q))
    questions = q[rand:rand+3]
    while len(questions) != 3:
        r = random.randrange(0, len(q))
        questions.append(q[r])
    return render_template("index.html", questions=questions)
