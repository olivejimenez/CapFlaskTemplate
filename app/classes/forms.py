# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of of a class. Forms are managed by the 
# Flask-WTForms library.

from tkinter.tix import Select
from flask.app import Flask
from flask import flash
from flask_wtf import FlaskForm
from mongoengine.fields import EmailField, IntField 
import mongoengine.errors
#from wtforms.fields.html5 import URLField, DateField, DateTimeField, EmailField
from wtforms.validators import URL, NumberRange, Email, Optional, InputRequired, ValidationError, DataRequired, EqualTo
from wtforms import PasswordField, StringField, SubmitField, validators, TextAreaField, HiddenField, IntegerField, SelectField, FileField, BooleanField
from app.classes.data import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])  
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        try:
            User.objects.get(username=username.data)
        except mongoengine.errors.DoesNotExist:
            flash(f"{username.data} is available.")
        else:
            raise ValidationError('This username is taken.')

    def validate_email(self, email):
        try:
            User.objects.get(email=email.data)
        except mongoengine.errors.DoesNotExist:
            flash(f'{email.data} is a unique email address.')
        else:
            raise ValidationError('This email address is already in use. if you have forgotten your credentials you can try to recover your account.')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Status',choices=[("New to film","New to film"),("Knows some of the classics","Knows some of the classics"),("Somewhat of a film bro","Somewhat of a film bro"),("Criterion Collection watcher only","Criterion Collection watcher only")])

class PostForm(FlaskForm):
    title = StringField('Movie', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    genre = SelectField('Genre', choices=[("comedy","comedy"),("horror","horror"),("drama","drama"),("experimental","experimental")])
    review = TextAreaField('Post', validators=[DataRequired()])
    rating = SelectField('review', choices = [("1 star", "1 star"),("2 stars", "2 stars"),("3 stars", "3 stars"),("4 stars", "4 stars"),("5 stars","5 stars")])
    submit = SubmitField('Post')
   
class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')