from flask import render_template, request
from flask.views import MethodView

from forms.bill_form import BillForm
from models.bill import Bill
from models.flatmate import Flatmate


class BillFormView(MethodView):
    """
    BillFormView handles GET and POST requests for the bill form page.
    """

    def get(self):
        """
        Handles GET requests.
        Initializes a new BillForm and renders the bill form template.
        """
        bill_form = BillForm()
        return render_template('bill-form.html', bill_form=bill_form)

    def post(self):
        """
        Handles POST requests.
        Processes the form data, calculates the bill split, and renders the results.
        """
        # Initialize the BillForm with data from the request.
        bill_form = BillForm(request.form)

        # Extract the amount and period from the form data.
        amount = float(bill_form.amount.data)
        period = bill_form.period.data

        # Extract the first flatmate's name and days in house.
        name1 = bill_form.name1.data
        dih1 = int(bill_form.days_in_house1.data)

        # Extract the second flatmate's name and days in house.
        name2 = bill_form.name2.data
        dih2 = int(bill_form.days_in_house2.data)

        # Create Bill and Flatmate objects based on the extracted data.
        bill = Bill(amount, period)
        flatmate1 = Flatmate(name=name1, days_in_house=dih1)
        flatmate2 = Flatmate(name=name2, days_in_house=dih2)

        # Render the bill form template with the results.
        return render_template('bill-form.html',
                               result=True,
                               bill_form=bill_form,
                               name1=name1, name2=name2,
                               amount1=flatmate1.pays(bill, flatmate2),
                               amount2=flatmate2.pays(bill, flatmate1))
