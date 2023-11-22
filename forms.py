from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, HiddenField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_wtf import FlaskForm
from models import User

class RegistrationForm(FlaskForm):
    """Registration form."""
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """Login form."""
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class DrinkSearchForm(FlaskForm):
    """Form for searching drinks"""

    drink_name = StringField('Drink Name')
    drink_glass = SelectField('Drink Glass', choices=[
        ('Highball glass', 'Highball glass'),
        ('Cocktail glass', 'Cocktail glass'),
        ('Old-fashioned glass', 'Old-fashioned glass'),
        ('Whiskey Glass', 'Whiskey Glass'),
        ('Collins glass', 'Collins glass'),
        ('Pousse cafe glass', 'Pousse cafe glass'),
        ('Champagne flute', 'Champagne flute'),
        ('Whiskey sour glass', 'Whiskey sour glass'),
        ('Cordial glass', 'Cordial glass'),
        ('Brandy snifter', 'Brandy snifter'),
        ('White wine glass', 'White wine glass'),
        ('Nick and Nora Glass', 'Nick and Nora Glass'),
        ('Hurricane glass', 'Hurricane glass'),
        ('Coffee mug', 'Coffee mug'),
        ('Shot glass', 'Shot glass'),
        ('Jar', 'Jar'),
        ('Irish coffee cup', 'Irish coffee cup'),
        ('Punch bowl', 'Punch bowl'),
        ('Pitcher', 'Pitcher'),
        ('Pint glass', 'Pint glass'),
        ('Copper Mug', 'Copper Mug'),
        ('Wine Glass', 'Wine Glass'),
        ('Beer mug', 'Beer mug'),
        ('Margarita/Coupette glass', 'Margarita/Coupette glass'),
        ('Beer pilsner', 'Beer pilsner'),
        ('Beer Glass', 'Beer Glass'),
        ('Parfait glass', 'Parfait glass'),
        ('Mason jar', 'Mason jar'),
        ('Margarita glass', 'Margarita glass'),
        ('Martini Glass', 'Martini Glass'),
        ('Balloon Glass', 'Balloon Glass'),
        ('Coupe Glass', 'Coupe Glass')
        ])
    drink_type = SelectField('Drink Type', choices=[
        ('Ordinary Drink', 'Ordinary Drink'),
        ('Cocktail', 'Cocktail'),
        ('Shake', 'Shake'),
        ('Other / Unknown', 'Other / Unknown'),
        ('Cocoa', 'Cocoa'),
        ('Shot', 'Shot'),
        ('Coffee / Tea', 'Coffee / Tea'),
        ('Homemade Liqueur', 'Homemade Liqueur'),
        ('Punch / Party Drink', 'Punch / Party Drink'),
        ('Beer', 'Beer'),
        ('Soft Drink', 'Soft Drink')
        ]) 
    selected_category = HiddenField('selected_category')

    drink_ingredients = SelectMultipleField('Drink Ingredients', choices=[
        ('Light rum', 'Light rum'),
        ('Applejack', 'Applejack'),
        ('Gin', 'Gin'),
        ('Dark rum', 'Dark rum'),
        ('Sweet Vermouth', 'Sweet Vermouth'),
        ('Strawberry schnapps', 'Strawberry schnapps'),
        ('Scotch', 'Scotch'),
        ('Apricot brandy', 'Apricot brandy'),
        ('Triple sec', 'Triple sec'),
        ('Southern Comfort', 'Southern Comfort'),
        ('Orange bitters', 'Orange bitters'),
        ('Brandy', 'Brandy'),
        ('Lemon vodka', 'Lemon vodka'),
        ('Blended whiskey', 'Blended whiskey'),
        ('Dry Vermouth', 'Dry Vermouth'),
        ('Amaretto', 'Amaretto'),
        ('Tea', 'Tea'),
        ('Champagne', 'Champagne'),
        ('Coffee liqueur', 'Coffee liqueur'),
        ('Bourbon', 'Bourbon'),
        ('Tequila', 'Tequila'),
        ('Vodka', 'Vodka'),
        ('Añejo rum', 'Añejo rum'),
        ('Bitters', 'Bitters'),
        ('Sugar', 'Sugar'),
        ('Kahlua', 'Kahlua'),
        ('demerara Sugar', 'demerara Sugar'),
        ('Dubonnet Rouge', 'Dubonnet Rouge'),
        ('Watermelon', 'Watermelon'),
        ('Lime juice', 'Lime juice'),
        ('Irish whiskey', 'Irish whiskey'),
        ('Apple brandy', 'Apple brandy'),
        ('Carbonated water', 'Carbonated water'),
        ('Cherry brandy', 'Cherry brandy'),
        ('Creme de Cacao', 'Creme de Cacao'),
        ('Grenadine', 'Grenadine'),
        ('Port', 'Port'),
        ('Coffee brandy', 'Coffee brandy'),
        ('Red wine', 'Red wine'),
        ('Rum', 'Rum'),
        ('Grapefruit juice', 'Grapefruit juice'),
        ('Ricard', 'Ricard'),
        ('Sherry', 'Sherry'),
        ('Cognac', 'Cognac'),
        ('Sloe gin', 'Sloe gin'),
        ('Apple juice', 'Apple juice'),
        ('Pineapple juice', 'Pineapple juice'),
        ('Lemon juice', 'Lemon juice'),
        ('Sugar syrup', 'Sugar syrup'),
        ('Milk', 'Milk'),
        ('Strawberries', 'Strawberries'),
        ('Chocolate syrup', 'Chocolate syrup'),
        ('Yoghurt', 'Yoghurt'),
        ('Mango', 'Mango'),
        ('Ginger', 'Ginger'),
        ('Lime', 'Lime'),
        ('Cantaloupe', 'Cantaloupe'),
        ('Berries', 'Berries'),
        ('Grapes', 'Grapes'),
        ('Kiwi', 'Kiwi'),
        ('Tomato juice', 'Tomato juice'),
        ('Cocoa powder', 'Cocoa powder'),
        ('Chocolate', 'Chocolate'),
        ('Heavy cream', 'Heavy cream'),
        ('Galliano', 'Galliano'),
        ('Peach Vodka', 'Peach Vodka'),
        ('Ouzo', 'Ouzo'),
        ('Coffee', 'Coffee'),
        ('Spiced rum', 'Spiced rum'),
        ('Water', 'Water'),
        ('Espresso', 'Espresso'),
        ('Angelica root', 'Angelica root'),
        ('Orange', 'Orange'),
        ('Cranberries', 'Cranberries'),
        ('Johnnie Walker', 'Johnnie Walker'),
        ('Apple cider', 'Apple cider'),
        ('Everclear', 'Everclear'),
        ('Cranberry juice', 'Cranberry juice'),
        ('Egg yolk', 'Egg yolk'),
        ('Egg', 'Egg'),
        ('Grape juice', 'Grape juice'),
        ('Peach nectar', 'Peach nectar'),
        ('Lemon', 'Lemon'),
        ('Firewater', 'Firewater'),
        ('Lemonade', 'Lemonade'),
        ('Lager', 'Lager'),
        ('Whiskey', 'Whiskey'),
        ('Absolut Citron', 'Absolut Citron'),
        ('Pisco', 'Pisco'),
        ('Irish cream', 'Irish cream'),
        ('Ale', 'Ale'),
        ('Chocolate liqueur', 'Chocolate liqueur'),
        ('Midori melon liqueur', 'Midori melon liqueur'),
        ('Sambuca', 'Sambuca'),
        ('Cider', 'Cider'),
        ('Sprite', 'Sprite'),
        ('7-Up', '7-Up'),
        ('Blackberry brandy', 'Blackberry brandy'),
        ('Peppermint schnapps', 'Peppermint schnapps'),
        ('Creme de Cassis', 'Creme de Cassis')
        ]) 
    submit = SubmitField('Search')



# MIGHT ADD THIS LATER

# class DrinkAddForm(FlaskForm):
#    """Form for adding drinks."""

#    drink_name = StringField('Drink Name', validators=[DataRequired()])
#    drink_type = StringField('Drink Type', validators=[DataRequired()])
#    drink_ingredients = StringField('Drink Ingredients', validators=[DataRequired()])
#    drink_instructions = StringField('Drink Instructions', validators=[DataRequired()])

