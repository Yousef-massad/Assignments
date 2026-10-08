from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'counter_secret_key'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)