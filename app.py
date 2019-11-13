import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myRecipes'
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    recipes=mongo.db.recipes.find().sort([('views-per-page', DESCENDING)]).limit(3)
    return render_template('index.html', title="Home", recipes=recipes)
    
    
@app.route('/recipe-listing')
def recipe_listing():
    recipes=mongo.db.recipes.find()
    return render_template('recipe-listing.html', title="Recipes", recipes=recipes)
    
    
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """Shows full recipe and increments view"""
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    recipe_ingredients = mongo.db.recipes.recipe_ingredients.find_one()
    recipe = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe )

  
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


