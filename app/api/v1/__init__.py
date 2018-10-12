from flask import Flask, Blueprint
from flask_restful import Api, Resource
from .views.views import Orders, Cart

blue = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(blue)


api.add_resource(Orders, '/orders/<int:id>')
api.add_resource(Cart, '/orders')
