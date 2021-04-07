import os
from flask import Blueprint, Flask, render_template, request, redirect, flash, url_for, session, send_from_directory
from flask_login import UserMixin, login_user, logout_user, current_user, login_required
from datetime import date, timedelta
from werkzeug.utils import secure_filename
import os
import json

#app imports
from app import app, login_manager
from app.forms import LoginForm, SignupForm, RecipeForm, SearchRecipeForm, AddToKitchenForm
from ..system_functions import populate_database, query_database, update_database
import gc

user = Blueprint("user", __name__)
#JASON TEST routes, will soon create a blueprint for this
@user.route('/')
@user.route('/')
def index():
    form = LoginForm()
    return render_template("login.html", form=form)

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
            user_ = User(query_database.getUser(email=email))
            # print(user)
            if (user_ is not None) and (password == user_.get_password()):
                remember_me = False

                if 'remember_me' in request.form:
                    remember_me = True
                
                # get user id, load into session
                login_user(user_, remember=remember_me)

                # flash a message to the user
                flash('Logged in successfully.', 'success')
                
                return redirect(url_for("user.meal_plan")) 
        else:
            flash('Username or Password is incorrect.','danger')
    
    flash_errors(form)
    return render_template("login.html", form=form)



@user.route('/recipe/<recipeid>')
@login_required
def recipe(recipeid):
    recipe = query_database.getRecipe(recipeid)
    # print('RECIPE',recipe[0])
    return render_template("recipe.html", recipe=recipe)


@user.route('/add-recipe', methods=["GET", "POST"])
@login_required
def add_recipe():
    """displaying the form to add a new recipe"""
    #this function is just a idea of what should be done

    if request.method == 'POST':

        # Note the difference when retrieving form data using Flask-WTF
        # Here we use myform.firstname.data instead of request.form['firstname']
        name = request.form['name']

        # Get file data and save to your uploads folder
        # photo = recipe_form.photo.data
        photo = request.files['image']

        filename = secure_filename(photo.filename)
        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        )
        photo.save(filepath)

        ingredients = json.loads(request.form['ingredients'])
        instructions = json.loads(request.form['instructions'])
        

        # Add new property to database
        #to do
        update_database.addRecipe(
            {
                "name": name, 
                "image":filename, 
                "added_by":current_user.get_id(),
                "ingredients": ingredients,
                "instructions":instructions
            }
        )

        flash('Recipe added successfully.', 'success')
        return redirect(url_for('user.add_recipe'))
    return render_template("input_recipe.html")


@user.route('/meal_plan')
@login_required
def meal_plan():
    
    today = date.today() #todays date

    #stores the dates of the current week into an array
    dates = [today + timedelta(days=i) for i in range(-1 - today.weekday(), 6 - today.weekday())]
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    
    #dates of the current week formatted as a string
    f_date = [days[fdate.weekday()]+", "+months[fdate.month-1]+" "+str(fdate.day)+"th" for fdate in dates]
    
    #format dates for use in database query
    fdb_dates = []
    for fdb_date in dates:
        string = str(fdb_date.year) + "-"
        if fdb_date.month < 10:
            string += '0' +str(fdb_date.month)
        else:
            string += str(fdb_date.month)

        string += '-'
        if fdb_date.day < 10:
            string += '0' + str(fdb_date.day)
        else:
            string += str(fdb_date.day)

        fdb_dates.append(string)
    
    user_id = current_user.get_id()
    # print(fdb_dates)
    #get meals from database grouped by date
    meals=[]
    for date_ in fdb_dates:
        meals.append(query_database.getMealsForDate(user_id, date_))

    # print('Meals',meals)
    # print('User id',user_id)
    # meals = query_database.getMealPlan(user_id,startDate,endDate)

    return render_template("meal_plan.html", dates=f_date, fdb_dates=fdb_dates, meals=meals)


@user.route('/browse_recipes', methods=["GET", "POST"])
@login_required
def browse_recipes():
    form = SearchRecipeForm()
    current_count = current_user.get_recipe_count()
    recipes = query_database.getNRecipes(current_count,current_count+27)
    current_user.increase_recipe_count(27)
    
    if request.method == "POST" and form.validate_on_submit():
        search = form.email.data
        return render_template("browse_recipes.html", form=form, recipes=recipes)
    return render_template("browse_recipes.html", form=form, recipes=recipes)


@user.route('/browse_foods', methods=["GET","POST"])
@login_required
def browse_foods():
    print(gc.isenabled())
    addform = AddToKitchenForm()
    form = SearchRecipeForm()
    current_count = current_user.get_recipe_count()
    foods = query_database.getNFoodItems(current_count,current_count+27)
    current_user.increase_recipe_count(27)
    
    if request.method == "POST" and form.validate_on_submit():
        search = form.email.data
        return render_template("browse_foods.html", form=form,addform=addform, foods=foods)
    return render_template("browse_foods.html", form=form, addform=addform,foods=foods)


@user.route('/add_to_kitchen/<foodid>/<units>/<quantity>', methods=['GET'])
@login_required
def add_to_kitchen(foodid,units,quantity):
    
    print("Add to Kitchen",current_user.get_id(),foodid,units,quantity)
    update_database.insertFoodInKitchenStock(current_user.get_id(),foodid,units,quantity)
    return json.dumps({"success":"Adding was a success"})


@user.route('/grocery')
@login_required
def grocery():
    today = date.today() #todays date
    dates = [today + timedelta(days=i) for i in range(-1 - today.weekday(), 6 - today.weekday())]
    #format dates for use in database query
    fdb_dates = []
    for fdb_date in dates:
        string = str(fdb_date.year) + "-"
        if fdb_date.month < 10:
            string += '0' +str(fdb_date.month)
        else:
            string += str(fdb_date.month)

        string += '-'
        if fdb_date.day < 10:
            string += '0' + str(fdb_date.day)
        else:
            string += str(fdb_date.day)

        fdb_dates.append(string)

    mlist = query_database.generateSupermarketList(current_user.get_id(),fdb_dates[0], fdb_dates[-1])
    print(mlist)

    return render_template("grocery.html",mlist=mlist)

@user.route('/kitchen')
@login_required
def kitchen():
    kitchen = query_database.getKitchenStock(current_user.get_id())
    food_data = [(food['food_name'],food['calories_per_ml'], food['calories_per_g']) for food in kitchen]
    return render_template("Kitchen.html", food_data=food_data)


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
    print(id)
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
        self.recipe_cnt_for_browse_recipe = 0
    # Overriding get_id is required if you don't have the id property
    # Check the source code for UserMixin for details
    def get_id(self):
        object_id = self.user_dict['user_id']
        return str(object_id)
    
    def get_password(self):
        print(self.user_dict)
        return self.user_dict['password']
    
    def get_recipe_count(self):
        return self.recipe_cnt_for_browse_recipe

    def increase_recipe_count(self,val):
        self.recipe_cnt_for_browse_recipe+=val
    
    def reset_recipe_count(self):
        self.recipe_cnt_for_browse_recipe=0
###
# 
###



# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)
