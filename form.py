from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateRecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name...', validators=[DataRequired()])
    recipe_description = TextAreaField('Recipe Description...', validators=[DataRequired()])
    recipe_ingredients = TextAreaField('Recipe Ingredients (Seperate each list item with a fullstop)...', validators=[DataRequired()])
    recipe_instructions = TextAreaField('Recipe Instructions (Seperate each list item with a fullstop)...', validators=[DataRequired()])
    recipe_image_url = StringField('Recipe Image URL...', validators=[DataRequired()])
    submit = SubmitField('Create Recipe')