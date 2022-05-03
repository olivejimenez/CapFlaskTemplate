from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Post
from app.classes.forms import PostForm
from flask_login import login_required
import datetime as dt

# This route actually does two things depending on the state of the if statement 
# 'if form.validate_on_submit()'. When the route is first called, the form has not 
# been submitted yet so the if statement is False and the route renders the form.
# If the user has filled out and succesfully submited the form then the if statement
# is True and this route creates the new post based on what the user put in the form.
# Because this route includes a form that both gets and posts data it needs the 'methods'
# in the route decorator.
@app.route('/post/new', methods=['GET', 'POST'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def postNew():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = PostForm()

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new post form. 
        # Post() is a mongoengine method for creating a new post. 'newPost' is the variable 
        # that stores the object that is the result of the Post() method.  
        newPost = Post(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            subject = form.subject.data,
            content = form.content.data,
            author = current_user.id,
            review = form.subject.data,
            # This sets the modifydate to the current datetime.
            modifydate = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        newPost.save()

        # Once the new post is saved, this sends the user to that post using redirect.
        # and url_for. Redirect is used to redirect a user to different route so that 
        # routes code can be run. In this case the user just created a post so we want 
        # to send them to that post. url_for takes as its argument the function name
        # for that route (the part after the def key word). You also need to send any
        # other values that are needed by the route you are redirecting to.
        return redirect(url_for('post',postID=newPost.id))

    # if form.validate_on_submit() is false then the user either has not yet filled out
    # the form or the form had an error and the user is sent to a blank form. Form errors are 
    # stored in the form object and are displayed on the form. take a look at postform.html to 
    # see how that works.
    return render_template('postform.html',form=form)
