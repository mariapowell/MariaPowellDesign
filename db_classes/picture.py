import webapp2
from google.appengine.ext import ndb
import db_definitions as db #Contain Classes Used By Website
import json

class Picture(webapp2.RequestHandler):
	def get(self):
		#Validation


		picture = db.Picture.query().fetch()
		if payment == None:
			self.response.status = 400
			self.response.status_message = "Pictures Not Found"
			self.response.write(self.response.status)
			return

		for p in payment:
			out = 
