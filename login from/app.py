from flask import Flask, render_template, request, send_file,redirect,session
import pandas as pd
import mysql.connector
import os



app = Flask(__name__)
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host="127.0.0.1",user='root',password='',database='user')

cursor=conn.cursor() ##database communication with cursor


# @app.route('/')
# def index():
    # return render_template('index.html')

# @app.route('/download')
# def Download_file():
	# p="jiomart.csv"
	# return send_file(p,as_attachment=True)

@app.route('/')
def login():

	return render_template('login.html')


@app.route('/register')
def about():
	return render_template('register.html')


@app.route('/home')
def home():
	if 'user_id' in session:
		return render_template('home.html')
	else:
		return redirect('/')

	


@app.route('/login_validation',methods=['POST'])
def login_validation():
	email=request.form.get('email')
	password=request.form.get('password')

	cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """ .format(email,password))

	user=cursor.fetchall()

	if len(user)>0:
		session['user_id']=user[0][0]
		return redirect('/home')

	else:
		return redirect('/')


	if user == session.pop('user_id'):
		return redirect('/')
	else:
		return redirect('/home')



@app.route('/add_user',methods=['POST'])
def add_user():
	name=request.form.get('uname')
	email=request.form.get('uemail')
	password=request.form.get('upassword')

	cursor.execute("""INSERT INTO `users`(`user_id`, `name`, `email`, `password`) VALUES (NULL,'{}','{}','{}')""".format(name,email,password))
	conn.commit()

	cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE  '{}' """.format(email))
	myuser=cursor.fetchall()
	session['user_id']=myuser[0][0]
	return  redirect('/home')

@app.route('/logout')
def logout():
	session.pop('user_id')
	return redirect('/')






if __name__ == '__main__':
    app.run(debug=True)
