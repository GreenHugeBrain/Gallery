from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, InputRequired


class AddProduct(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    img = FileField('Image', validators=[FileRequired(), FileAllowed(['jpeg', 'jpg', 'png', 'webp'])])
    submit = SubmitField('Add Product')
    
class EditProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    img = FileField('Product Image')
    submit = SubmitField('Update Product')

class RemoveProductForm(FlaskForm):
    submit = SubmitField('Remove Product')

#  validators=[DataRequired()]