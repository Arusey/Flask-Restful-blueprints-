import unittest
from ... import app

class TestOrder(unittest.TestCase):
	"""docstring for TestOrder"""
	def setup(self):
		self.app = app
		self.app.test_client()
		self.data = {}
		
	def test_get_order(self):
		response = self.app.get

	def teardown(self):
		pass