from flask import Flask, jsonify, render_template, request, redirect, flash
from flask.helpers import url_for

app = Flask(__name__)
app.secret_key = 'secret'

# global 
users = [
    {'spongebob': 'squarepants'},
    {'sandy': 'cheeks'},
    {'patrick': 'star'},
    {'larry': 'lobster'}
]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/auth', methods=["POST"])
def auth():
    usernm = request.form.get('username')
    passwrd = request.form.get('password')
    checked = request.form.get('checkbox')
    
    #toggle on means log in
    if checked== 'on':
        if (usernm == "" or usernm == " "):
            flash("Invalid input.", 'error')
            return redirect(url_for('login'))

        for dic in users:
            for key in dic:
                if usernm == key:
                    flash("Username already taken. Try a different one!", 'error')
                    return redirect(url_for('login'))
            
        users.append({usernm: passwrd})
        flash("User added. You can log in now.")
        return redirect(url_for('login'))
    
    #toggle null means sign up 
    else:
        for dic in users:
            for key in dic:
                if usernm == key and passwrd == dic[key]:
                    flash("Successfully logged in.", 'successful')
                    return redirect(url_for('index'))
        flash("Invalid credentials.", 'error')
        return redirect(url_for('login'))

@app.route('/signOut')
def signOut():
    flash("Successfully logged out.", 'success')
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')