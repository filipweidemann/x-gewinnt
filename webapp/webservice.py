from flask import Flask, flash, redirect, url_for, session, logging, request
from flask import render_template
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from werkzeug.utils import secure_filename
from gevent.wsgi import WSGIServer
from game import game
import os


app = Flask(__name__)
app.secret_key = 'some_secret_key_very_diffucult___wow'

class Create(Form):
    width = StringField('Enter the width of your board.', [validators.input_required('Please enter the desired width.')])
    height = StringField('Enter the height of your board.', [validators.input_required('Please enter the desired height.')])
    win_length = StringField('Enter the length of consecutive tokens needed to claim the win', [validators.input_required('Please enter the desired win length.')])
    starting_player = StringField('Who will start? x or o?', [validators.input_required('Please enter x or y.')])

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/leaderboards')
def leaderboards():
    return render_template('leaderboards.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = Create(request.form)
    #import pdb; pdb.set_trace()
    if request.method == 'POST' and form.validate():
        width = int(form.width.data)
        height = int(form.height.data)
        win_length = int(form.win_length.data)
        starting_player = form.starting_player.data
        session['current_game'] = game.Board(width, height, None, win_length).__dict__
        current_game = session.get('current_game')
        current_game['turn_color'] = str(starting_player)
        return redirect('play')
    else:
        return render_template('create.html', form=form)

@app.route('/play')
def play():
    current_game = session.get('current_game')
    #import pdb; pdb.set_trace()
    if current_game is None:
        flash('You don\'t have any unfinished games! Please start a new one.', 'danger')
        return redirect('/')
    height = current_game['height']
    width = current_game['width']
    game_state = current_game['game_state']
    won_by = current_game['won_by']
    if won_by != None:
        session.clear()
        return render_template('winnerwinnerchickendinner.html', won_by = won_by)
    return render_template('play.html', height = int(height), width = int(width), game_state = game_state)

@app.route('/drop/<row>/')
def perform_token_drop(row):
    current_game = session.get('current_game')
    #import pdb; pdb.set_trace()
    height = current_game['height']
    width = current_game['width']
    game_state = current_game['game_state']
    win = current_game['win_length']
    drop_color = current_game['turn_color']

    current_game = game.Board(int(width), int(height), game_state, int(win))
    token = current_game.drop(drop_color, int(row))
    #import pdb; pdb.set_trace()
    session['current_game'] = current_game.__dict__
    return redirect('play')

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
