from flask import Flask, request, render_template, session, jsonify
# from forms import SearchForm
from datetime import datetime
import os

from helper_functions import exception_logger
import db_query

app = Flask(__name__)

app.secret_key = 'AGSJYWVSUjyfuyfYWSyfda'



@app.route('/', methods=['GET','POST'])
def home():
	try:

		return render_template('index.html'), 200

	except Exception as e:
		exception_logger()


@app.route('/enter_details', methods=['GET','POST'])
def details():

	try:
		session['name'] = request.form['name']
		session['age'] = request.form['age']
		session['gender'] = request.form['gender']
		# del session['csrf_token']

		db_query.create_table_and_db()

		date_entered = db_query.enter_emp_details(name=session['name'], gender=session['gender'], age=session['age'])


		if date_entered:
			return jsonify({"message":"data entered successfully", "status":"success"}), 200

	except Exception as e:
		exception_logger()
		return jsonify({"message":"something went wrong", "status":"failure"}), 400


if __name__ == '__main__':
	app.run(debug=True, port=5000)


