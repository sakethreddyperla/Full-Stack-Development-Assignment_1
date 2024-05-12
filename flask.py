from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store user credentials (In real-world, you would use a database)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    if username in users:
        return "Username already exists. Please choose another one."
    else:
        users[username] = password
        return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return "Signin successful. Welcome, {}!".format(username)
        else:
            return "Invalid username or password. Please try again."
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
