import datetime

from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms.fields.simple import StringField, SubmitField
from wtforms.form import Form
from models.bill import Bill
from models.flatmate import Flatmate

app = Flask(__name__)


class HomeView(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormView(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill-form.html', bill_form=bill_form)

    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.amount.data

        name1 = bill_form.name1.data
        dih1 = int(bill_form.days_in_house1.data)

        name2 = bill_form.name2.data
        dih2 = int(bill_form.days_in_house2.data)

        bill = Bill(amount, period)
        flatmate1 = Flatmate(name=name1, days_in_house=dih1)
        flatmate2 = Flatmate(name=name2, days_in_house=dih2)
        return render_template('bill-form.html',
                               result=True,
                               bill_form=bill_form,
                               name1=name1, name2=name2,
                               amount1=flatmate1.pays(bill, flatmate2),
                               amount2=flatmate2.pays(bill, flatmate1))


class BillForm(Form):
    amount = StringField('Bill Amount:', default="100")
    period = StringField('Bill Period:', default=datetime.datetime.utcnow().strftime("%B %d, %Y"))
    name1 = StringField('Name: ')
    days_in_house1 = StringField('Days in the House: ')
    name2 = StringField('Name: ')
    days_in_house2 = StringField('Days in the House: ')
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomeView.as_view('home'))
app.add_url_rule('/bill', view_func=BillFormView.as_view('bill'))

app.run(debug=True)
