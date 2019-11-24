import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myRecipes'
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    """This shows a list of 3 recipes which have the highest views"""
    recipes=mongo.db.recipes.find().sort([('views', DESCENDING)]).limit(3)
    return render_template('index.html', title="Home", recipes=recipes)
    
    
@app.route('/recipe_listing')
def recipe_listing():
    """This shows a list of all of the recipes"""
    recipes=mongo.db.recipes.find()
    return render_template('recipe-listing.html', title="Recipes", recipes=recipes)
    
    
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """This shows all fields in recipes & increments the views by 1"""
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    recipe_ingredients = mongo.db.recipes.recipe_ingredients.find_one()
    recipe = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe)
    
    
@app.route('/create_recipe')
def create_recipe():
    """This shows a list of all of the recipes"""
    recipes_db = mongo.db.recipes
    return render_template('create-recipe.html')
    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """This will add each field to the database"""
    recipe_db = mongo.db.recipes
    # This is insert a new value for each field
    recipe_db.insert_one(request.form.to_dict())
    return redirect(url_for('recipe_listing'))
    
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipes_db = mongo.db.recipes.find_one({ '_id': ObjectId(recipe_id) })
    return render_template('edit-recipe.html', recipe=recipes_db)
    
  
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


