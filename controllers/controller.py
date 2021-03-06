from flask import render_template
from app import app
from models.player import Player
from models.game import Game
import random

@app.route('/')
def index():
    return render_template('index.html', title='Home', stage='Player 1: Make your move!')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/<id>/')
def player_1_choice(id):
    choice_p1 = id.lower().strip()
    choices = Game().choices
    if choice_p1 in choices:
        return render_template('index.html', currentpath=id ,title='In-Game', stage='Player 2: Make your move!')
    else:
        return page_not_found(404)

@app.route('/<id1>/<id2>/')
def player_2_choice(id1, id2):
    choice_p1 = id1.lower().strip()
    choice_p2 = id2.lower().strip()
    result = Game.determine_winner(choice_p1, choice_p2)
    if result == None:
        return render_template("404.html")
    else:
        return render_template('index.html', title='Results!', stage=result, again=' Player 1, make your move!',  reset='/')

@app.route('/rules/')
def rules():
    return render_template('rules.html', title='Rules')

@app.route('/pve/')
def pve_home():
    return render_template('pve.html')

@app.route('/pve/<id>/')
def pve_result(id):
    choice_player = id.lower().strip()
    choice_cpu = random.choice(Game().choices)
    result = Game.determine_winner_cpu(choice_player, choice_cpu)
    if result == None:
        return render_template("404.html")
    else:
        return render_template('pve.html', title='Results!', stage=result, again='Go again!',  reset='/pve/')


