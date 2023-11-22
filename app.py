from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from forms import RegistrationForm, LoginForm, DrinkSearchForm
from models import User, LikedDrink
from passlib.hash import bcrypt
from flask_migrate import Migrate
from collections.abc import Mapping
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'catsArePrettyCool'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/capstoneproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.auto_reload = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.template_filter('tojson_safe')
def tojson_safe(obj):
    """Custom filter to make the object JSON serializable."""
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    return str(obj)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Form validated!")
        print("Form data:")
        print("Username:", form.username.data)
        print("Password:", form.password.data)

        hashed_password = bcrypt.hash(form.password.data)
        new_user = User(username=form.username.data, hashed_password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    else:
        print("Form not validated!")
        print("Form data:")
        print("Username:", form.username.data)
        print("Password:", form.password.data)
        flash('Account creation unsuccessful. Please check your username and password and try again.', 'danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.verify(form.password.data, user.hashed_password):
            login_user(user, remember=False)
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'error')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    liked_drinks = LikedDrink.query.filter_by(user_id=current_user.id).all()
    drink_details = [fetch_drink_details(liked_drink.drink_id) for liked_drink in liked_drinks]
    return render_template('profile.html', current_user=current_user, liked_drinks=liked_drinks, drink_details=drink_details)

@app.route('/drinksearch', methods=['GET', 'POST'])
# @login_required
def drinksearch():
    form = DrinkSearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Get form data
        drink_name = form.drink.data
        drink_category = form.category.data
        drink_glass = form.glass.data
        drink_ingredients = form.ingredients.data

        # Perform a database query to search for drinks based on the form data
        query = db.session.query(Drink)

        if drink_name:
            query = query.filter(Drink.name.ilike(f'%{drink_name}%'))
            print(drink_name)
        if drink_category:
            query = query.filter(Drink.category == drink_category)
            print(drink_category)
        if drink_glass:
            query = query.filter(Drink.glass == drink_glass)
            print(drink_glass)
        if drink_ingredients:
            for ingredient in drink_ingredients:
                query = query.filter(Drink.ingredients.ilike(f'%{ingredient}%'))

        # Execute the query and get the results
        results = query.all()
        print(f"Is User Authenticated: {current_user.is_authenticated}")

        return render_template('drinksearch.html', form=form, results=results, currentUser=current_user)

    # Handle selected category from featured categories
    selected_category = request.args.get('category')
    if selected_category:
        form.selected_category.data = selected_category
        print(f"Is User Authenticated: {current_user.is_authenticated}")
    return render_template('drinksearch.html', form=form, currentUser=current_user)


@app.route('/add-to-liked/<drink_id>', methods=['POST'])
@login_required  
def add_to_liked(drink_id):
    # Create a LikedDrink instance and add it to the user's liked drinks
    user = current_user 
    liked_drink = LikedDrink(user_id=user.id, drink_id=drink_id)
    db.session.add(liked_drink)
    db.session.commit()
    return {'message': 'Drink added to liked drinks'}

@app.route('/remove-from-liked/<drink_id>', methods=['POST'])
@login_required
def remove_from_liked(drink_id):
    user = current_user
    session = db.session

    liked_drink = session.query(LikedDrink).filter_by(user_id=user.id, drink_id=drink_id).first()

    if liked_drink:
        try:
            session.delete(liked_drink)
            session.commit()
            return {'message': 'Drink removed from liked drinks'}, 200 
        except Exception as e:
            # Rollback the session in case of an error
            session.rollback()
            return {'message': 'Failed to remove drink from liked drinks', 'error': str(e)}, 500  
        finally:
            session.close()
    else:
        return {'message': 'Drink not found in liked drinks'}, 404

def fetch_drink_details(drink_id):
    api_url = f'https://thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data['drinks'][0] if data['drinks'] else None
    else:
        return None 

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)






