from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')

# In-memory dictionary for storing users (for demonstration purposes)
users = {
    'username': 'password123',
    'password': 'letmein',
}

@app.route('/')
def index():
    return "Welcome to the Flask Login and Add User App!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    message2 = request.args.get('message2') 
    message1 = None  # Initialize message as None
    if request.method == 'POST':
        message2 = None
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            message1 = "Login successful! Welcome, " + username
        else:
            message1 = "Login failed. Please check your username and password."
    return render_template('login.html', message1=message1,message2=message2)

@app.route('/registration', methods=['GET', 'POST'], endpoint='registration')
def registration():
    message2 = None  # Initialize message as None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        message2 = "User added successfully!"
        return redirect(url_for('login') + f'?message2={message2}')
        #return render_template('login.html', message2=message2, message1=None)
    else:
        return render_template('registration.html', message2=message2, message1=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
