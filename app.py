import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
from forms import CreateRecipeForm

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myRecipes'
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    """This shows a list of 3 recipes which have the highest views"""
    recipes=mongo.db.recipes.find().sort([('views-per-page', DESCENDING)]).limit(3)
    return render_template('index.html', title="Home", recipes=recipes)
    
    
@app.route('/recipe-listing')
def recipe_listing():
    """This shows a list of all of the recipes"""
    recipes=mongo.db.recipes.find()
    return render_template('recipe-listing.html', title="Recipes", recipes=recipes)
    
    
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """Shows all fields in recipes & increments the views by 1"""
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    recipe_ingredients = mongo.db.recipes.recipe_ingredients.find_one()
    recipe = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe)
    
@app.route('/create_recipe', methods=['GET', 'POST'])
def create_recipe():
    create_recipe_form = CreateRecipeForm(request.form)
    
    recipes_db = mongo.db.recipes
    # insert the new recipe
    recipes_db.insert_one({
        'recipe_name': request.form['recipe_name'],
        'recipe_description': request.form['recipe_description'],
        'recipe_ingredients': request.form['recipe_ingredients'],
        'recipe_instrictions': request.form['recipe_instrictions'],
        'recipe_image_url': request.form['recipe_image_url'],
        'views': 0
    })
    return redirect(url_for('index', title='New recipe has been created'))
    return render_template('create-recipe.html', title="Create Recipe")

  
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


