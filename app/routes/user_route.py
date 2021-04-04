from flask import Blueprint, Flask, render_template, request, redirect, flash, url_for, session
from flask_login import UserMixin, login_user, logout_user, current_user, login_required
from datetime import date, timedelta
from werkzeug.utils import secure_filename
import os

#app imports
from app import app, login_manager
from app.forms import LoginForm, SignupForm, RecipeForm
from ..system_functions import populate_database, query_database, update_database


user = Blueprint("user", __name__)

#JASON TEST routes, will soon create a blueprint for this
@user.route('/')
def index():
    return render_template("login.html")

@user.route('/sign-up',methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('user.meal_plan'))
    
    form = SignupForm()
    if request.method == "POST" and form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        password = form.password.data
        rpassword = form.rpassword.data

        if password == rpassword:

            result = populate_database.insertUser({'fname':fname, 'lname':lname,\
                                                'email':email,'password':password})
            if result == True:
                # flash a message to the user
                flash('Sign up successful.', 'success')
                return redirect(url_for("user.login")) 
            elif result ==False:
                flash('Email address is already associated with an account','danger')
            else:
                flash('Database connection error','danger')
        else:
            flash('Passwords does not match','danger')
    return render_template("sign_up.html", form=form)


@user.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.meal_plan'))
    
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email and password:
            user = User(query_database.getUser(email=email))
            # print(user)
            if (user is not None) and (password == user.get_password()):
                remember_me = False

                if 'remember_me' in request.form:
                    remember_me = True
                
                # get user id, load into session
                login_user(user, remember=remember_me)

                # flash a message to the user
                flash('Logged in successfully.', 'success')
                
                return redirect(url_for("user.meal_plan")) 
        else:
            flash('Username or Password is incorrect.','danger')
    
    flash_errors(form)
    return render_template("login.html", form=form)



@user.route('/recipe/<recipe_name>')
@login_required
def recipe(recipe_name):
    return render_template("recipe.html", recipe_name=recipe_name)


@user.route('/add-recipe', methods=["GET", "POST"])
@login_required
def add_recipe():
    """displaying the form to add a new recipe"""
    #this function is just a idea of what should be done
    recipe_form = RecipeForm()

    if request.method == 'POST':
        if recipe_form.validate_on_submit():
            # Note the difference when retrieving form data using Flask-WTF
            # Here we use myform.firstname.data instead of request.form['firstname']
            name = recipe_form.name.data

            # Get file data and save to your uploads folder
            photo = recipe_form.photo.data

            filename = secure_filename(photo.filename)
            filepath = os.path.join(
                app.config['UPLOAD_FOLDER'], filename
            )
            photo.save(filepath)

            # Add new property to database
            #to do
            update_database.addRecipe({"name": name, "image":filepath, "added_by":current_user.get_id()})

            flash('Recipe added successfully.', 'success')
            return redirect(url_for('user.add_recipe'))

        flash_errors(recipe_form)
    return render_template("input_recipe.html", form=recipe_form)



@user.route('/meal_plan')
@login_required
def meal_plan():
    today = date.today()
    dates = [today + timedelta(days=i) for i in range(-1 - today.weekday(), 6 - today.weekday())]
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    
    f_date = [days[fdate.weekday()]+", "+months[fdate.month-1]+" "+str(fdate.day)+"th" for fdate in dates]
    return render_template("meal_plan.html", dates=f_date, meals={'date':1})


@user.route('/browse_recipes')
@login_required
def browse_recipes():
    return render_template("browse_recipes.html")


@user.route('/grocery')
@login_required
def grocery():
    pass


@user.route('/kitchen')
@login_required
def kitchen():
    pass


@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('user.login'))


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User(query_database.getUser(id=id))


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


#Wrapper User Class for user dict to use for flask login manager
class User(UserMixin):
    def __init__(self, user_dict):
        self.user_dict = user_dict

    # Overriding get_id is required if you don't have the id property
    # Check the source code for UserMixin for details
    def get_id(self):
        object_id = self.user_dict['user_id']
        return str(object_id)
    
    def get_password(self):
        print(self.user_dict)
        return self.user_dict['password']

###
# The functions below should be applicable to all Flask apps.
###


# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)
