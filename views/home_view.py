from flask import render_template
from flask.views import MethodView


class HomeView(MethodView):
    """
    HomeView handles GET requests for the home page.
    """

    def get(self):
        """
        Handles GET requests.
        Renders the home page template.
        """
        return render_template('index.html')
