from flask import Flask , render_template

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', boxnum=8, bg="red")

@app.route('/<num>')
def col(num):
    return render_template('index.html', boxnum=int(num), bg="red")

if __name__ == "__main__":
    app.run(debug=True)