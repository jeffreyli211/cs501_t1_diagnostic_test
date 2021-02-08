# project/server/users/view_users.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class UsersAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):
        # user_emails = db.session.query('').column_descriptions
        emails = db.session.query(User.email).all()
        parsed_emails = []
        for i in range(len(emails)):
          parsed_emails.append(emails[i][0])

        responseObject = {
    		  "All users": parsed_emails
        }
        return make_response(jsonify(responseObject)), 201


# define the API resources
all_users_view = UsersAPI.as_view('viewusers_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=all_users_view,
    methods=['GET']
)