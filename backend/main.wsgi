import api
import argparse

#
application = api.app
arg_parser = argparse.ArgumentParser()

# Switch between standalone and uwsgi configuration
if __name__ == '__main__':
	print('RadioWCSpy started main')
	from paste import httpserver
	
	arg_parser.add_argument('--host', default='127.0.0.1', help='IP address binding [127.0.0.1]')
	arg_parser.add_argument('--port', default='8001', help='TCP listening port [80]')
	arg_parser.add_argument('--db_uri', default='localhost', help='Database URI')
	arg_parser.add_argument('--db_port', default=28015, help='Database port')
	args = arg_parser.parse_args()

	application.config = vars(args)
	httpserver.serve(application, host=args.host, port=args.port)
else:
	print('RadioWCSpy started wsgi')
	
	arg_parser.add_argument('--site_name', help='Site name', nargs='*', default=['local'])
	arg_parser.add_argument('--db_uri', default='localhost', help='Database URI')
	arg_parser.add_argument('--db_port', default=28015, help='Database port')
	args = arg_parser.parse_args()

	# configure uwsgi application
	application.config = vars(args)
	
