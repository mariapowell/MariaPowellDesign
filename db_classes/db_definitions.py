from google.appengine.ext import ndb

#Picture Class Database Model
class Picture(ndb.Model):
	name = ndb.StringProperty(required=True)
	leftInStock = ndb.IntegerProperty(required=True)
	description = ndb.StringProperty()
	price = ndb.IntegerProperty(required=True)
	amountSold = ndb.IntegerProperty(required=True)
    blob_key = ndb.BlobKeyProperty(required=True) #picture access

	def to_dict(self):
			d = super(Picture, self).to_dict()
			d['key'] = self.key.id()
			return d