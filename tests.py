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


def test_recipes(self):
    """Test recipe list page loading"""
    res = self.client.get('/recipe-listing')
    data = res.data.decode('utf-8')
    assert res.status == '200 OK'
    assert 'features' in data

print("All tests passed")