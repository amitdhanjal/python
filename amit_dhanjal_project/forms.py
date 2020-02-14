from flask_wtf import Form
from wtforms import TextField, SubmitField, StringField, IntegerField
from wtforms import validators, ValidationError

class SearchForm(Form):

	name = TextField("Enter the name", [validators.Required("Please enter the name.")])
	gender = StringField("Enter the gender")
	age = IntegerField("Enter the age")
	submit = SubmitField("Submit")