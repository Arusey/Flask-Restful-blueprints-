from flask import Flask, Blueprint
from flask_restful import Api, Resource
from .views.views import Orders, Cart, SignUp, Login

blue = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(blue)

api.add_resource(Login, '/login')
api.add_resource(SignUp, '/users')
api.add_resource(Orders, '/orders/<int:id>')
api.add_resource(Cart, '/orders')
