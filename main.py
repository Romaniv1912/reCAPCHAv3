from flask import Flask, request, render_template
import requests

app = Flask(__name__)

SITE_KEY = '6LfhORsbAAAAAEL5B1yJbiyY5oFRhzDyuVkHxAvf'
SECRET_KEY = '6LfhORsbAAAAABQ0VYNoriBbMut4yb930Wwg0ICN'


#фукция для получения результата капчи
@app.route("/get_score", methods=['POST'])
def get_score():
	url = 'https://www.google.com/recaptcha/api/siteverify?secret=' + SECRET_KEY + '&response=' + request.form.get("TOKEN")
	response = requests.get(url)
	return response.json()


@app.route("/",  methods=['GET', 'POST'])
def hello_world():
	return render_template("main.html", SITE_KEY=SITE_KEY)


app.run(host='localhost', port=3000)
