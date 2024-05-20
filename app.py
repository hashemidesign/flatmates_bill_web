from flask import Flask

from views.bill_view import BillFormView
from views.home_view import HomeView

app = Flask(__name__)

app.add_url_rule('/', view_func=HomeView.as_view('home'))
app.add_url_rule('/bill', view_func=BillFormView.as_view('bill'))

if __name__ == "__main__":
    app.run(debug=True)
