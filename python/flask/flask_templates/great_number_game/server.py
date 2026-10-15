from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['game_status'] = None
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_number():
    try:
        user_guess = int(request.form['guess'])
    except ValueError:
        return redirect('/')

    if user_guess > session['number']:
        session['game_status'] = 'too_high'
    elif user_guess < session['number']:
        session['game_status'] = 'too_low'
    else:
        session['game_status'] = 'correct'

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=8000)