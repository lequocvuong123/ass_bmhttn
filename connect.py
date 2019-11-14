import cx_Oracle
from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

conn=cx_Oracle.connect('system','duong123')
cur = conn.cursor()

@app.route('/')
def index():
	return render_template('form.html')

# @app.route('/', methods=['POST'])
# def getvalue():
# 	name = request.form['name']
# 	address = request.form['address']
# 	gender  = request.form['gender ']
# 	cmnd = request.form['cmnd']
# 	phone = request.form['phone']
# 	email = request.form['email']
	
# 	return render_template('add.py', name=name,address=address,gender =gender ,cmnd=cmnd,phone=phone,email=email)
@app.route('/', methods=['POST'])
def insert():
	if request.method == "POST":
		name = request.form['name']
		address = request.form['address']
		gender  = request.form['gender']
		cmnd  = request.form['cmnd']
		phone  = request.form['phone']
		email  = request.form['email']

		cur.execute("INSERT INTO passport (name, address, gender,cmnd,phone,email,status) VALUES('"+ name +"','"+ address +"','"+ gender +"','"+ cmnd +"','"+ phone +"','"+ email +"','Cho XT')" )
		conn.commit()
if __name__ == '__main__':
	app.run(debug=True)