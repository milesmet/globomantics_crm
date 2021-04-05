class BusinessCustomer:

	def __init__(self, acct_id, money_owed):
		self.acct_id = acct_id
		self.money_owed = money_owed

	def update(self):
		if self.money_owed > 0:
			print(f"{self.acct_id}: Call companies fincnace department")
		else:
			print(f"{self.acct_id}: corporate balance paid")

class ConsumerCustomer:

	def __initi__(self, acct_id, money_owed):
		self.acct_id = acct_id
		self.money_owed = money_owed

	def update(self):
		if self.money_owed > 0:
			print(f"{self.acct_id}: Send polite reminder emaily")
		else:
			print(f"{self.acct_id}: individual lbalance paid")


