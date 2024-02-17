from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def main():

	return render_template("index.html")

@app.route('/', methods = ['POST'])

def math_operations():

	text = request.form['text']
	operation = request.form['operation']

	API = 'https://newton.now.sh/api/v2//' + operation + '/' + equation

	data = requests.get(API).json()

	answer = data['API']

	return render_template("index.html", result = API, equation = equation)

if __name__ == "__main__":

	app.run()