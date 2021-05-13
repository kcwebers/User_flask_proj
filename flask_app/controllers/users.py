# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

##############################################
# Show all route
##############################################
@app.route("/")
def index():
    return render_template("index.html", all_users = User.all_users())

##############################################
# Show one route
##############################################

@app.route("/show/<int:id>")
def show(id):
    data = {
        "id" : id
    }
    return render_template("show.html", user = User.one_user(data))

##############################################
# Create routes
##############################################

# render the create.html which houses the form
@app.route("/create")
def create():
    return render_template("create.html")

# process the infro from our form on create.html, then redirect elsewhere
@app.route("/create_friend", methods=["POST"])
def create_friend():
    data = {
        "fname":request.form['fname'],
        "lname":request.form['lname'],
        "occupation":request.form['occ']
    }
    User.save(data)
    return redirect('/')

##############################################
# Delete one route
##############################################

@app.route("/delete/<id>")
def delete(id):
    mysql = connectToMySQL('first_flask')
    query = "DELETE FROM friends WHERE id=%(id)s;"
    data = {
        "id" : int(id)
    }
    mysql.query_db(query, data)
    return redirect("/")

##############################################
# Edit one route
##############################################

# renders edit.html with the form
@app.route("/edit/<int:id>")
def edit(id):
    mysql = connectToMySQL('first_flask')
    query = "SELECT * FROM friends WHERE id=%(id)s;"
    data = {
        "id" : int(id)
    }
    user = mysql.query_db(query, data)
    return render_template("edit.html", user = User.edit_user(data))

# processes the info attained from the form
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = {
        "first_name" : request.form['fname'],
        "last_name" : request.form['lname'],
        "occupation" : request.form['occ'],
        "id" : id
    }
    User.update_user(data)
    return redirect(f"/show/{id}")
