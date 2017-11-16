from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired


class SpectrumUploadForm(FlaskForm):
    file = FileField(validators=[FileRequired()])