"""
Autor: Matias Martelossi
Creation: 17/09/2022
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class PersonForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('LastName', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    photo = StringField('Photo')
    send = SubmitField('Send')


class PublicationForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description')
    priority = StringField('Priority')
    publication = StringField('Publication')
    # Internal info
    status = StringField('Status')
    time_published = StringField('Time Published')
    user = StringField('User')
    created_at = DateTimeField('Created')
    updated_at = DateTimeField('Updated')

