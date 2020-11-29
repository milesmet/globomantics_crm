class Database:
	def __init__(self, path):
		with open(path, "r") as handle:
			#import json #std library in python
			#self.data = json.load(handle) #loads and reads from file
			#import yaml
			#self.data = yaml.safe_load(handle)
			import xmltodict
			self.data = xmltodict.parse(handle.read()) ["root"]
			print(self.data)

	def balance(self, acct_id):
		acct = self.data.get(acct_id)
		if acct:
			bal = float(acct["due"]) - float(acct["paid"])
			#
			return f"{bal:.2f} USD"
			#return int(acct["due"]) - int(acct["paid"])
		return None