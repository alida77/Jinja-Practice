from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=number, current_year=year)


@app.route('/guess/<name>')
def guess(name):
    param = {"name": name}
    gender_response = requests.get(url="https://api.genderize.io", params=param).json()
    gender = gender_response["gender"]
    age_response = requests.get(url="https://api.agify.io", params=param).json()
    age = age_response["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    all_posts = requests.get("https://api.npoint.io/a1b494d9228a42e32553").json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
