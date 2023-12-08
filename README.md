# CapstoneProject1: TheCocktailDB Club

The primary goal of the website is to provide cocktail enthusiasts with a user-friendly platform to discover and save cocktail recipes based on their preferred ingredients using a combination of HTML, Javascript, Python, and PostgreSQL. It should facilitate easy user registration, authentication, and the ability to create a personalized cocktail recipe collection. The website's target demographic will include individuals of legal drinking age (typically 21 and older) who have an interest in cocktails and mixology. Users may range from beginners looking for simple recipes to experienced bartenders seeking inspiration for unique creations. The website will utilize data from a TheCocktailDB API, which contains details about cocktail recipes, ingredients, preparation instructions, and glass-types.

My database consists of tables for user accounts and saved recipes:
- User Table: UserID (Primary Key), Username, Password (Hashed and Salted)
- Recipe Table: RecipeID (Primary Key), DrinkID, UserID

Potential issues with the API might include rate limiting, data accuracy, and availability. 
The only sensitive information stored is the password. I currently use bcrypt for that.

The app currently includes the following key features:
- User registration and authentication.
- Search for cocktails based on ingredients.
- Save favorite recipes to a user's account.
- View and edit saved recipes.

Stretch goals (currently not implemented):
- User-generated content add interactivity
- A recommendation system based on user preferences/ currently saved recipies
- A rating system
