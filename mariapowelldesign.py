import os
import urllib
import jinja2
import webapp2

# Python Template Engine To Render my HTML
JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True
	)

# call the home page html template
class HomePage(webapp2.RequestHandler):
	template_variables = {}

	def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render())

	#def post(self):
	#	self.template_variables['form_content'] = {}
	#	template = JINJA_ENVIRONMENT.get_template('home.html')

		#For every element that came with the request -> can view them in the browser
	#	for i in self.request.arguments():
	#		self.template_variables['form_content'][i] = self.request.get(i)
		#Add in stuff step by step
	#	p = Picture(name=self.request.get('txt_name'),
	#				leftInStock=self.request.get('int_leftInStock'),
	#				picture=self.request.get('img_blobKey'),
	#				description=self.request.get('txt_description'),
	#				price=self.request.get('int_price'),
	#				amountSold=self.request.get('int_amountSold'),
	#	p.put()

	#	result = Picture.query().fetch()

	#	self.response.write(template.render(result))


#class Admin(webapp2.RequestHandler):
#	template_variables = {}

#	def get(self):
#		template = JINJA_ENVIRONMENT.get_template('admin.html')
#		self.response.write(template.render())


# starts the application
application = webapp2.WSGIApplication([
	('/', HomePage),
#	('/admin', Admin),
], debug=True)