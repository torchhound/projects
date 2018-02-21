import os, linecache, tokenize
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import Form 
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from flask.ext.bcrypt import Bcrypt

DEBUG = True #will need to be turned to False in production

app = Flask(__name__)
app.secret_key = 'pseudorandom' #might need to be instanced for security
bcrypt = Bcrypt(app)

dbName = "users.txt"

def getPreviousUid(file):
	return linecache.getline(file, 1)
'''		
def getCurrentLine(file):
	return linecache.getline(tokenize.open(file), 2)
'''			
def replaceLine(fileName, lineNum, text): #might need to be replaced if performance becomes an issue
    lines = open(fileName, 'r').readlines() #why does this not replace the correct line?
    lines[lineNum] = text
    out = open(fileName, 'w')
    out.writelines(lines)
    out.close()

class user(): 
	uid = ""
	username = ""
	email = ""
	pwdhash = "" 
   
	def __init__(self, username, email, password):
		uid = int(getPreviousUid(dbName)) + 1
		username = username
		self.email = email.lower()
		self.set_password(password)
		replaceLine(dbName, 1, getPreviousUid(dbName) + str(1)) #why does this not replace the correct line?
		#replaceLine(dbName, 2, getCurrentLine(dbName) + 1)
     
	def set_password(self, password):
		self.pwdhash = bcrypt.generate_password_hash(password) 
   
	def check_password(self, password): #currently unnecessary
		return bcrypt.check_password_hash(self.pwdhash, password)
			
	def export(self):
		self.uid = str(self.uid)
		self.username = str(self.username)
		self.email = str(self.email)
		self.password = str(self.pwdhash)
		exportData = "[%s, %s, %s, %s]" % (self.uid, self.username, self.email, self.password) #uid and username not writing or not being initialized
		return exportData

class signupForm(Form):
	username = TextField("Username",  [validators.Required("Please enter your username.")])
	email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	submit = SubmitField("Create account")
 
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
 
	def validate(self):
		if not Form.validate(self):
			return False
	
		nameCheck = str(self.username) #does capitalization matter for linux usernames?
		if nameCheck in open(dbName, 'r').read(): #check if username has been used before
			self.username.errors.append("That username is already taken")
			return False
		else:
			return True
	
		emailCheck = self.email.lower() 
		if emailCheck in open(dbName, 'r').read(): #check if email has been used before
			self.email.errors.append("That email is already taken")
			return False
		else:
			return True	
 
@app.route('/')
def index():
	"""renders the home page template"""
	return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register(): #still needs to create an account on server and to email login credentials upon signup 
	"""renders the register template""" #would be nice to have automated password resets and automated payment checking
	form = signupForm(csrf_enabled = False) #might need to be changed in production
	if request.method == 'POST':
		if form.validate() == False:
			return render_template("register.html", form=form)
		else:   
			newUser = user(form.username.data, form.email.data, form.password.data)
			newUserExport = newUser.export()
			fW = open(dbName, 'a')
			fW.write(newUserExport) 
			fW.write("\n")
			flash("User successfully created!")
			return render_template("register.html", form=form)
	elif request.method == 'GET':
		return render_template("register.html", form=form)
		
if __name__ == "__main__":
	app.run()