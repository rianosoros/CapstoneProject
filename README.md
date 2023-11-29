# CapstoneProject1
1.  The primary goal of the website is to provide cocktail enthusiasts with a user-friendly platform to discover and save cocktail recipes based on their preferred ingredients. It should facilitate easy user registration, authentication, and the ability to create a personalized cocktail recipe collection.

2. The website's target demographic will include individuals of legal drinking age (typically 21 and older) who have an interest in cocktails and mixology. Users may range from beginners looking for simple recipes to experienced bartenders seeking inspiration for unique creations.

3. The website will utilize data from a cocktail API, which should contain details about cocktail recipes, ingredients, preparation instructions, and possibly user-generated content such as ratings and reviews.

4a. The database will consist of tables for user accounts, saved recipes, and possibly user-generated content like reviews or comments (If I am confident enough to get there).       - User Table: UserID (Primary Key), Username, Password (Hashed and Salted)
Recipe Table: RecipeID (Primary Key), Title, Ingredients, Instructions

4b. Potential issues with the API might include rate limiting, data accuracy, and availability. I will need to test a lot and be sure my error handling will account for all scenarios.

4c. The only sensitive information stored is the password. I plan to use bcrypt for that.

4d. The app will include the following key features:
      - User registration and authentication.
      - Search for cocktails based on ingredients.
      - Save favorite recipes to a user's account.
      - View and edit saved recipes.
      - User-generated content like ratings and reviews (not too sure about this yet).

4e.     1. User registers or logs in.
        2. After logging in, the user can search for cocktails by ingredients.
        3. They can save their favorite recipes to their account.
        4. They can view or delete their saved recipes.

4f.   - User-generated content add interactivity.
      - A recommendation system based on user preferences, and adding the rating system could be a stretch goal.
