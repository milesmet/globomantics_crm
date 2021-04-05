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


class AccountingSystem:

	def __init__(self):
		self.customers = set()

	def register(self, customer):
		self.customers.add(customer)

	def unregister(self, customer):
		self.customers.remove(customer)

	def notify(self):
		for customer in self.customers:
			customer.update()

def main():
	cust1 = BusinessCustomer("Acct11", 10)
	cust2 = BusinessCustomer("Acct2202", 0)
	cust3 = BusinessCustomer("Acct33", -10)
	cust4 = BusinessCustomer("Acct4400", 10)


	accounting_sys = AccountingSystem()
	accounting_sys.register(cust1)
	accounting_sys.register(cust2)
	accounting_sys.register(cust3)
	accounting_sys.register(cust4)

	accounting_sys.notify()

	accounting_sys.unregister(cust2)

	accounting_sys.notify()

if __name__ == "__main__":
	main()
