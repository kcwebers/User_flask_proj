from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dog import Dog
from flask_app.models.friend import Friend

##############################################
# Create routes
##############################################

# render the create.html which houses the form
@app.route("/new")
def new():
    return render_template("dogs/create.html", all_friends = Friend.all_friends())

# process the infro from our form on create.html, then redirect elsewhere
@app.route("/create_dog", methods=["POST"])
def create_dog():
    data = {
        "name":request.form['name'],
        "description":request.form['desc'],
        "friend_id":request.form['friend_id']
    }
    Dog.save_dog(data)
    return redirect('/')
