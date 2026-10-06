from flask import Flask
app=Flask(__name__)
@app.route('/')

def hello():
    return "Hello World!"

@app.route('/champion')
def ch():
    return "Champion!"

@app.route('/say/<name>')
def say(name):
    return f"hi {name}"

@app.route('/repeat/<num>/<name>')
def repeat(num,name):
    return name*int(num)


if __name__ == "__main__":
    app.run(debug=True)
    
