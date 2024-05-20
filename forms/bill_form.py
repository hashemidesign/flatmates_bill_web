from datetime import datetime

from wtforms.fields.simple import StringField, SubmitField
from wtforms.form import Form


class BillForm(Form):
    """
    BillForm is a FlaskForm that collects details about a bill to split between two flatmates.
    """
    # Field for the total amount of the bill with a default value of "100".
    amount = StringField('Bill Amount:', default="100")

    # Field for the billing period with the current date as the default value.
    period = StringField('Bill Period:', default=datetime.utcnow().strftime("%B %d, %Y"))

    # Field for the name of the first flatmate.
    name1 = StringField('Name: ')

    # Field for the number of days the first flatmate has stayed in the house.
    days_in_house1 = StringField('Days in the House: ')

    # Field for the name of the second flatmate.
    name2 = StringField('Name: ')

    # Field for the number of days the second flatmate has stayed in the house.
    days_in_house2 = StringField('Days in the House: ')

    # Submit button to calculate the bill split.
    button = SubmitField("Calculate")
