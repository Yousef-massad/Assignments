from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/play')
def box():
    return render_template('index.html', boxnum=int(3))

@app.route('/play/<x>')
def box2(x):
    return render_template('index.html', boxnum=int(x))

@app.route('/play/<x>/<color>')
def box3(x,color):
    return render_template('index.html', boxnum=int(x), box_color=color)


if __name__ == "__main__":
    app.run(debug=True)