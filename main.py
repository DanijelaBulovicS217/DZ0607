from flask import Flask, render_template,redirect, url_for, request, session
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import hashlib
import time

import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="raspored"
    )
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
@app.route('/raspored')
def prikazi_raspored():
		mycursor=mydb.cursor()
		mycursor.execute("SELECT * FROM tabela")
		data = mycursor.fetchall()
		return render_template('raspored.html', data=data)










if __name__ == '__main__':
	app.run(debug=True)