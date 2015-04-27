import webapp2
import handlers

routes = [
	('/', handlers.HelloWebapp2),
	('/api/changes', handlers.Changes),
	('/api/recent', handlers.Recent),
	(r'/api/recent/<page:\d+>', handlers.Recent),
	('/api/genres', handlers.Genres),
	('/api/count', handlers.Count)
]

app = webapp2.WSGIApplication(routes, debug=True)

app.error_handlers[404] = handlers.handle_404
app.error_handlers[500] = handlers.handle_500
