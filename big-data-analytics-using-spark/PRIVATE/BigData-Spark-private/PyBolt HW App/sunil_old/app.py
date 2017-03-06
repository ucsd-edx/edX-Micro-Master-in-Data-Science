from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import User


app = Flask(__name__)
app.secret_key='mykey'


@app.route('/')

@app.route('/welcome')
def welcome():
	if session['username'] is None:
		return redirect(url_for('login'))
    	return ("Hello " + session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
	error=None
	if request.method=='POST':
		uname=request.form['username']
		password=request.form['password']
		if uname==None or uname=="":
			error="Please Enter a UserName"
		elif password==None or password=="":
			error="Please Enter a Password"
		else:	
			user=User(uname,password)
			if user.is_authenticated:
				session['username']=uname
				return redirect(url_for('welcome'))
			else:
				error="Invalid Credentials!!"
				session['username']=None		
	return render_template('login.html',error=error)

@app.route("/logout", methods=["GET"])
def logout():
	if session['username'] is None:
		return redirect(url_for('login'))
	session['username']=None
	return redirect(url_for("login"))

if __name__ == '__main__':
	app.run(debug=True)



