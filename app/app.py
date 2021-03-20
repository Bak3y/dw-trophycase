from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def rootpath():
	return render_template('index.html')

@app.route('/health')
def health():
	return "OK"

@app.route('/userAdd', methods=["GET", "POST"])
def userAdd():
    if request.method == 'POST':
        result = request.form
        username = result['username']
        return render_template('userAdd.html', username = username)

@app.route('/userSearch', methods=["GET", "POST"])
def userSearch():
    if request.method == 'POST':
        result = request.form
        username = result['username']
        return render_template('userSearch.html', username = username)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
