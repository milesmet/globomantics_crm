from flask import Flask, render_template, request
import os
os.chdir('C:/Users/Miles.Metelerkamp/Dropbox/Studying/Cisco DevNet/Flask/')
from database import Database
#create flask object and instatiate db object
app = Flask(__name__)
#path="data/db.json"
path="data/db.xml"
db = Database(path)


@app.route("/", methods=["GET", "POST"])
def index():
	#this 4 button clicks
	if request.method == "POST":
		acct_id = request.form["acct_id"]
		acct_balance = db.balance(acct_id.upper())
		app.logger.debug(f'balance from {acct_id}: {acct_balance}')

	else:
		acct_balance = "N/A"

	return render_template("index.html", acct_balance=acct_balance)

if __name__ == "__main__":
		app.run()