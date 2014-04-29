from google.appengine.ext import db

class Listing(db.Model):
	username = db.StringProperty(multiline=True)
	name = db.StringProperty(multiline=True)
	year = db.StringProperty(multiline=True)
	section	= db.StringProperty(multiline=True)
	title = db.StringProperty(multiline=True)
	category = db.StringProperty(multiline=True)
	description	 = db.TextProperty()
	partcipant_count = db.StringProperty(multiline=True)
	donor_list = db.StringProperty(multiline=True)
	email = db.StringProperty(multiline=True)
	opening_bid = db.StringProperty(multiline=True)