from flask import Flask, render_template ,request ,session,json,redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash
import webview
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_login import UserMixin
import os
from datetime import datetime

# Flask constructor takes the name of

# current module (__name__) as argument.
app = Flask(__name__)

with open('conf.json','r') as c:
    params=json.load(c) ["params"]

app.secret_key="super-secret-key"
app.config['UPLOAD_FOLDER']=params['uploader_location']
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql://root:@localhost/plantparadise"
# app.config['SQLALCHEMY_MODIFICATION']=True
db=SQLAlchemy(app)
class Contacts(db.Model):
		sno = db.Column(db.Integer, primary_key=True)
		fname=db.Column(db.String(80),nullable=False)
		lname = db.Column(db.String(120),nullable=False)
		email = db.Column(db.String(120), nullable=False)
		message = db.Column(db.String(120),nullable=False)
		date = db.Column(db.String(120),nullable=True)

class Login(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		username=db.Column(db.String(80),nullable=False)
		userrole = db.Column(db.String(120),nullable=False)
		password = db.Column(db.String(120), nullable=False)

@app.route('/contact', methods=['GET','POST'])
def contact():
	if(request.method=="POST"):
		fname=request.form.get('firstname')
		lname=request.form.get('lastname')
		email=request.form.get('email')
		message=request.form.get('message')
		entry=Contacts(fname=fname,lname=lname,email=email,message=message,date=datetime.now())
		db.session.add(entry)
		db.session.commit()
	return render_template("contact1.html")	

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def frontpage():
	return render_template("frontpage.html")

@app.route('/frontpage2')
# ‘/’ URL is bound with hello_world() function.
def frontpage2():
	return render_template("frontpage2.html")

@app.route('/mainlogin',methods=["GET","POST"])
# ‘/’ URL is bound with hello_world() function.
def mainlogin():
	return render_template("mainlogin.html")


@app.route('/about')
# ‘/’ URL is bound with hello_world() function.
def about():
	return render_template("about.html")
@app.route('/loginpage',methods=["GET","POST"])
# ‘/’ URL is bound with hello_world() function.
def loginpage():
	# if request.method == "POST":
	# 	username =request.form['username']
	# 	userrole = request.form['userrole']
	# 	password = request.form['password']
	# 	user =Login.query.filter_by(id=id).first()
	# 	if user is not None:
	# 		return render_template("frontpage.html")
		return render_template("loginpage.html")
	
@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
	if request.method=="POST":
		username=request.form.get('usrname')
		userpass=request.form.get('psw')
		if(username == params['admin_user'] and userpass == params['admin_pass']):
			session['user'] = username
			contacts=Contacts.query.all()
			signups=Signup.query.all()
			payments=Payment.query.all()
			cuspays=Cuspay.query.all()
			return render_template("dashboard.html",params=params,contacts=contacts,signups=signups,payments=payments,cuspays=cuspays)
	return render_template("Adminlogin.html",params=params)

class Signup(db.Model):
		sno = db.Column(db.Integer, primary_key=True)
		uname=db.Column(db.String(80),nullable=False)
		email = db.Column(db.String(120), nullable=False)
		passwd = db.Column(db.String(120), nullable=False)
		date = db.Column(db.String(120),nullable=True)

# @app.route('/uploader',methods=["GET","POST"])
# def uploader():
# 	if ('user' in session and session['user']==params['admin_user']):
# 		if(request.method=="POST"):
# 			 f=request.files['file']
# 			 f.save(os.path.join(app.config['UPLOAD_FOLDER']),secure_filename(f.filename))
# 			 return "uploaded successfully"
@app.route('/signup',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def signup():
	if ('user' in session and session['user']==params['admin_user']):
		if(request.method=="POST"):
			f=request.files['file']
			f.save(os.path.join(app.config['UPLOAD_FOLDER']),secure_filename(f.filename))
			uname=request.form.get('usrname')
			email=request.form.get('email')
			passwd=request.form.get('psw')
			signup=Signup(uname=uname,email=email, passwd=passwd,date=datetime.now())
			db.session.add(signup)
			db.session.commit()
		return render_template("loginpage.html")
	return render_template("signup.html")


class Review(db.Model):
		sno = db.Column(db.Integer, primary_key=True)
		message= db.Column(db.String(120), nullable=False)
		date= db.Column(db.String(120),nullable=True)

		
		
@app.route('/Review',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def Review():
	if(request.method=="POST"):
		message=request.form.get('message')
		review=Review(message=message,date=datetime.now())
		db.session.add(review)
		db.session.commit()
	return render_template("Review.html")


@app.route('/manageuser')
# ‘/’ URL is bound with hello_world() function.
def manageuser():
	return render_template("manageuser.html")
	
# categaory  
@app.route('/hibiscous')
# ‘/’ URL is bound with hello_world() function.
def hibiscous():
	return render_template("hibiscous.html")


@app.route('/lily')
# ‘/’ URL is bound with hello_world() function.
def lily():
	return render_template("lily.html")


@app.route('/rose')
# ‘/’ URL is bound with hello_world() function.
def rose():
	return render_template("rose.html")	

@app.route('/alovera')
# ‘/’ URL is bound with hello_world() function.
def alovera():
	return render_template("alovera.html")

@app.route('/home')
# ‘/’ URL is bound with hello_world() function.
def home():
	return render_template("home.html")

@app.route('/indoor')
# ‘/’ URL is bound with hello_world() function.
def indoor():
	return render_template("indoor.html")

@app.route('/neem')
# ‘/’ URL is bound with hello_world() function.
def neem():
	return render_template("neem.html")

@app.route('/tulsi')
# ‘/’ URL is bound with hello_world() function.
def tulsi():
	return render_template("tulsi.html")

@app.route('/Indoorplant')
# ‘/’ URL is bound with hello_world() function.
def Indoorplant():
	return render_template("Indoorplant.html")

@app.route('/deco')
# ‘/’ URL is bound with hello_world() function.
def deco():
	return render_template("deco.html")

@app.route('/bamboo')
# ‘/’ URL is bound with hello_world() function.
def bamboo():
	return render_template("bamboo.html")

@app.route('/forever')
# ‘/’ URL is bound with hello_world() function.
def forever():
	return render_template("forever.html")


@app.route('/home1')
# ‘/’ URL is bound with hello_world() function.
def home1():
	return render_template("home1.html")


@app.route('/canna')
# ‘/’ URL is bound with hello_world() function.
def canna():
	return render_template("canna.html")

@app.route('/forbes')
# ‘/’ URL is bound with hello_world() function.
def forbes():
	return render_template("forbes.html")

@app.route('/store')
# ‘/’ URL is bound with hello_world() function.
def store():
	return render_template("store.html")

# class Floweringplant(db.Model):
# 		price=db.Column(db.String(80),nullable=False)

@app.route('/floweringplants')
# ‘/’ URL is bound with hello_world() function.
def floweringplants():
	return render_template("floweringplants.html",params=params)		


@app.route('/money')
# ‘/’ URL is bound with hello_world() function.
def money():
	return render_template("money.html")		

@app.route('/livinggift')
# ‘/’ URL is bound with hello_world() function.
def livinggift():
	return render_template("livinggift.html",params=params)	

@app.route('/microgreen')
# ‘/’ URL is bound with hello_world() function.
def microgreen():
	return render_template("microgreen.html",params=params)	


# microgree seeds

@app.route('/Amaranthus')
# ‘/’ URL is bound with hello_world() function.
def Amaranthus():
	return render_template("Amaranthus.html")

@app.route('/Sunflower')
# ‘/’ URL is bound with hello_world() function.
def Sunflower():
	return render_template("Sunflower.html")

	
@app.route('/Basillemon')
# ‘/’ URL is bound with hello_world() function.
def Basillemon():
	return render_template("Basillemon.html")

@app.route('/Cabbage')
# ‘/’ URL is bound with hello_world() function.
def Cabbage():
	return render_template("Cabbage.html")

@app.route('/Radish')
# ‘/’ URL is bound with hello_world() function.
def Radish():
	return render_template("Radish.html")

@app.route('/Spinach')
# ‘/’ URL is bound with hello_world() function.
def Spinach():
	return render_template("Spinach.html")

@app.route('/PakChoy')
# ‘/’ URL is bound with hello_world() function.
def PakChoy():
	return render_template("PakChoy.html")

@app.route('/Lettuce')
# ‘/’ URL is bound with hello_world() function.
def Lettuce():
	return render_template("Lettuce.html")


@app.route('/bonsaiplant')
# ‘/’ URL is bound with hello_world() function.
def bonsaiplant():
	return render_template("bonsaiplant.html",params=params)

@app.route('/Bonsai')
# ‘/’ URL is bound with hello_world() function.
def Bonsai():
	return render_template("Bonsai.html")

@app.route('/Bon')
# ‘/’ URL is bound with hello_world() function.
def Bon():
	return render_template("Bon.html")

@app.route('/Branched')
# ‘/’ URL is bound with hello_world() function.
def Branched():
	return render_template("Branched.html")

@app.route('/Carmona')
# ‘/’ URL is bound with hello_world() function.
def Carmona():
	return render_template("Carmona.html")

@app.route('/Cherry')
# ‘/’ URL is bound with hello_world() function.
def Cherry():
	return render_template("Cherry.html")

@app.route('/Bonobibthi')
# ‘/’ URL is bound with hello_world() function.
def Bonobibthi():
	return render_template("Bonobibthi.html")


@app.route('/Organicplant')
# ‘/’ URL is bound with hello_world() function.
def Organicplant():
	return render_template("Organicplant.html",params=params)


@app.route('/miniatureplant')
# ‘/’ URL is bound with hello_world() function.
def miniatureplant():
	return render_template("miniatureplant.html",params=params)
	
@app.route('/cart')
# ‘/’ URL is bound with hello_world() function.
def cart():
	return render_template("cart.html")

class Cuspay(db.Model):
		sno = db.Column(db.Integer, primary_key=True)
		name=db.Column(db.String(80),nullable=False)
		cnum = db.Column(db.Integer, nullable=False)
		emonth = db.Column(db.String(80), nullable=False)
		eyear = db.Column(db.Integer, nullable=False)
		cVVno = db.Column(db.Integer, nullable=False)
		date = db.Column(db.String(120),nullable=True)

@app.route('/cutomerpayment',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def cutomerpayment():
	if(request.method=="POST"):
		name=request.form.get('name')
		cnum=request.form.get('number')
		emonth=request.form.get('month')
		eyear=request.form.get('eyear')
		cVVno=request.form.get('cardnum')
		cuspay=Cuspay(name=name,cnum=cnum,emonth=emonth,eyear=eyear,cVVno=cVVno,date=datetime.now())
		db.session.add(cuspay)
		db.session.commit()
		return redirect(url_for("frontpage2"))
	return render_template("cutomerpayment.html")
class Payment(db.Model):
		sno = db.Column(db.Integer, primary_key=True)
		name=db.Column(db.String(80),nullable=False)
		email= db.Column(db.String(120),nullable=False)
		phno = db.Column(db.String(120), nullable=False)
		address = db.Column(db.String(120),nullable=False)
		pname = db.Column(db.String(120),nullable=False)
		date = db.Column(db.String(120),nullable=True)

@app.route('/checked',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def checked():
	if(request.method=="POST"):
		name=request.form.get('name')
		email=request.form.get('email')
		phno=request.form.get('mobile')
		address=request.form.get('address')
		pname=request.form.get('pname')
		payment=Payment(name=name,email=email, phno=phno,address=address,pname=pname,date=datetime.now())
		db.session.add(payment)
		db.session.commit()
		return redirect(url_for("cutomerpayment"))
	return render_template("checked.html")


# main driver function
if __name__ == '__main__':
	# run() method of Flask class runs the application
	# on the local development server.

	app.run(debug=True)

