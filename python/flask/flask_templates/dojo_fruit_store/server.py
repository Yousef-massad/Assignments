from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    strawberry_count = int(request.form['strawberry'])
    raspberry_count = int(request.form['raspberry'])
    apple_count = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']

    total_count = strawberry_count + raspberry_count + apple_count
    current_time = datetime.now().strftime("%B %dth %Y %I:%M:%S %p")

    print(f"Charging {first_name} {last_name} for {total_count} fruits.")

    return render_template(
        "checkout.html",
        strawberry=strawberry_count,
        raspberry=raspberry_count,
        apple=apple_count,
        first_name=first_name,
        last_name=last_name,
        student_id=student_id,
        total=total_count,
        time=current_time
    )

if __name__ == "__main__":
    app.run(debug=True)