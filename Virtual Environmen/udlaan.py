from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UdlaanForm(FlaskForm):
    customerID = StringField("kunder ID")
    inventoryID = StringField("DVD Lager ID")
    staffID = StringField("Personale ID")
    submit = SubmitField("registrer")
