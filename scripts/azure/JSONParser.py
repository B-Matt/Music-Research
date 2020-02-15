import json

class JSONParser():
	def __init__(self, data):
		self.__dict__ = json.loads(data)
	
	def json_to_list(self, json_data):
		"""
			Converts JSON array into Python list.

			:param json_data: JSON array that needs conversion
			:return: Python list
		"""
		py_list = []
		for data in json_data:
			py_list.append(int(data))
		return py_list
