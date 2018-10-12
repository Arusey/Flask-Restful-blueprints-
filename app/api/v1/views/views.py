from flask import jsonify, make_response, request
from flask_restful import Resource

cart = []
users = []
class Cart(Resource):
	def post(self):
		id = len(cart) + 1
		data = request.get_json()
		name = data["name"]
		price = data["price"]

		total = {
			'id' : id,
			'name' : name,
			'price' : price
		}

		if data["name"] == "":
			return make_response(jsonify({
				"Message": "You Cannot Enter an empty product name",
				"Status": "No content"
				}, 204))

		cart.append(total)
		return make_response(jsonify({
			"Status" : "ok",
			"Message" : "Post Success",
			"My orders" : cart
			}, 201))


	def get(self):
		return cart

class SignUp(Resource):
	"""docstring for SignUp"""
	def post(self):
		data = request.get_json()
		id = len(users) + 1
		self.name = data['name'] 
		self.email = data['email']
		self.password = data['password']

		
		
		

		user = {
			"name" : self.name,
			"email" : self.email,
			"password" : self.password
		}

		users.append(user)
		return make_response(jsonify(
				{
				"Status": "ok",
				"Message" : "Account created Successfully",
				"user" : users
				} , 201
			))

class Login(Resource):
	def post(self):
		data = request.get_json()

		self.email = data["email"]
		self.password = data["password"]

		for user in users:
			if user["email"] == data["email"] and user["password"] == data["password"]:
				return make_response(jsonify(
						{
						'Status': "ok",
						"Message" : "Login Successful",
						"return" : user
						}, 200
					))



class Orders(Resource):
	def get(self, id):

		for product_id in cart:
			if product_id["id"] == id:
				return make_response(jsonify(
					{
						'Status': "ok",
						'Message': "Order Successful",
						"Order": product_id
					}, 200))
	def delete(self, id):

		for product in cart:
			if id == product["id"]:
				cart.remove(product)
				return make_response(jsonify(
					{
						"Status" : "ok",
						"Message" : "Successfully deleted",
						"orders" : cart
					}, 202))
	def put(self, id):

		data = request.get_json()
		name = data["name"]
		price = data["price"]

		for product in cart:
			if product["id"] == id:
				if name == "":
					return  make_response(jsonify(
						{ 
						"Status" : "No update",
						"Message" : "You cannot insert a blank name"
						}, 404
					))
				product["name"] = name
				product["price"] = price
				return make_response(jsonify(
						{
						"Status" : "updated",
						"Message": "Successfully updated",
						"Order" : cart
						}, 201
					))
			


				payload = {
					"name" : name,
					"price" : price
				}
				cart.append(payload)
				return cart, 201 



