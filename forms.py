from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email


class CreateSearchByFilterForm(FlaskForm):
    city = StringField("City")
    id = StringField("Id")
    name = StringField("Name")
    state = StringField("State")
    type = StringField("type (micro, nano, brewpub, large, bar, planning, regional, etc.)")
    per_page = StringField("Number of breweries to return each call.", validators=[DataRequired()])
    sort = StringField("Sort the results by one or more fields. (asc or desc)")
    submit = SubmitField("Submit")


class CreateSearchByQueryForm(FlaskForm):
    query = StringField("Query", validators=[DataRequired()])
    submit = SubmitField("Submit")
