from app import app
from models import *
from flask import render_template
from flask_security import login_required
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cardsdata')
@login_required
def cardsdata():
    carddata = Cards.query.all()
    return render_template("cardsdata.html", carddata=carddata)