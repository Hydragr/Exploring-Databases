from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):

	name=StringField("name of Company")
	id=IntegerField("Id of the Pilot")
	submit = SubmitField("Add Company")