from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():

    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    occupation = request.form.get('occupation')
    income = request.form.get('income')
    state = request.form.get('state')

    return render_template(
        'recommendations.html',
        name=name,
        age=age,
        gender=gender,
        occupation=occupation,
        income=income,
        state=state
    )

if __name__ == '__main__':
    app.run(debug=True)