'''
The classes in this file are used to test the business logic of recipe views and models
'''

import unittest
import re

from flask_pymongo import PyMongo

import app as app_module

app = app_module.app

# This is setting up a test db on mongo and switching CSRF off
app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False
app.config['MONGO_URI'] = 'mongodb://localhost:27017/recipesTesting'

mongo = PyMongo(app)
app_module.mongo = mongo

class AppTestCase(unittest.TestCase):
    """Test deleting everything in database"""
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            mongo.db.recipes.delete_many({})


class AppTests(AppTestCase):
    """Testing loading of home page"""
    def test_index(self):
        res = self.client.get('/')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Home' in data
        
    def test_recipes(self):
        """Test recipe list page loading"""
        res = self.client.get('/recipe-listing')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Recipes' in data
        
    def test_recipe_page(self):
        """Test finding a recipe and redirect to that recipes specific page"""
        res = self.client.get('/recipes')
        # Test regular expressions to locate Object id of a recipe
        recipe_id = re.findall(r'href="/recipe/(\w+)"', res.data.decode("utf8"))
        # Test to ensure it's populated
        assert len(recipe_id) > 0
        # Test to ensure that it is going to the correct recipe from the recipe_id
        res = self.client.get('/recipe/{}'.format(recipe_id[0]))
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Pumpkin rice' in data
        
    def test_search_page(self):
        """Test searching for a recipe and redirect to search page"""
        res = self.client.get('/search', follow_redirects=True, data={
            'recipe_name': 'Pumpkin rice',
            'recipe_description': 'From brownies and pancakes to veggie-packed curries, stir-fries and salads, these vegan recipes are vibrant and delicious.',
            'recipe_instructions': 'Add all of the ingredients',
            'recipe_keywords': 'vegan, pumpkin, rice, butternut squash'
        })
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'vegan' in data
        assert 'Pumpkin' in data
        assert 'delicious' in data
        assert 'butternut' in data  
        
    def test_create_recipe(self):
        """Test creating a recipe and check to make sure that new recipe is showing after redirecting"""
        res = self.client.post('/create_recipe', follow_redirects=True, data={
            'recipe_name': 'Pumpkin rice',
            'recipe_description': 'From brownies and pancakes to veggie-packed curries, stir-fries and salads, these vegan recipes are vibrant and delicious.',
            'recipe_ingredients': '400g pumpkin, or butternut squash',
            'recipe_instructions': 'Add all of the ingredients',
            'recipe_keywords': 'vegan, pumpkin, rice, butternut squash',
            'recipe_image_url': 'image url goes here'
        })
        data = res.data.decode('utf-8')
        assert 'vegan' in data
        assert 'Pumpkin' in data
        assert 'delicious' in data
        assert 'butternut' in data
        assert 'here' in data
        
    def test_delete_recipe(self):
        """Test deleteing a recipe and recipe is not found after page has redirected"""
        res = self.client.get('/recipes')
        # Test regular expressions to locate Object id of a recipe
        recipe_id = re.findall(r'href="/recipe/(\w+)"', res.data.decode("utf-8"))
        assert len(recipe_id) > 0
        # Delete recipe using the recipe_id
        res = self.client.post('/delete_recipe/{}'.format(recipe_id[0]), follow_redirects=True)
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Pumpkin rice' not in data
        
    def test_404_error(self):
        """Test 404 error page"""
        res = self.client.get('/handle_404')
        data = res.data.decode('utf-8')
        assert res.status == '404'
        assert 'Page not found' in data
    
print("All tests passed")