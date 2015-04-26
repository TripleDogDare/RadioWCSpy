import webapp2
import logging
import rethinkdb as r
import db_rethink as database

#TODO: runs on a single connection for now, will make a pool eventually
db = database.Database()
#connect, we're going to let any exceptions kill the process herp derp
db.configure()
db.connect()


def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! I could swear this page was here!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A server error occurred!')
    response.set_status(500)

class HelloWebapp2(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello, webapp2!')

class Changes(webapp2.RequestHandler):
	def get(self):
		# self.response.headers.add('Content-Type', 'text/event-stream')
		self.response.write('change stream not implented')

class Count(webapp2.RequestHandler):
	def get(self):
		try:
			data = db.count()
			self.response.headers.add('Content-Type', 'text/json')
			self.response.write( data )
		except Exception, e:
			handle_500(self.request, self.response, e)

class Recent(webapp2.RequestHandler):
	def get(self, page=0):
		try:
			data = db.recent(skip=page*100, qty=100)
			self.response.headers.add('Content-Type', 'text/json')
			self.response.write( data )
		except Exception, e:
			handle_500(self.request, self.response, e)

class Genres(webapp2.RequestHandler):
	def get(self):
		try:
			data =  db.count_genres()
			self.response.headers.add('Content-Type', 'text/json')
			self.response.write( data )
		except Exception, e:
			handle_500(self.request, self.response, e)
