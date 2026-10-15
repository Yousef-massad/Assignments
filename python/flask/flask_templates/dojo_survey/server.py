from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    gender = request.form.get('gender', 'Not specified')
    comment = request.form['comment']
    hobbies = request.form.getlist('hobbies')
    
    return render_template('result.html', name=name, location=location, language=language, gender=gender, comment=comment, hobbies=hobbies)

if __name__ == "__main__":
    app.run(debug=True, port=8000)