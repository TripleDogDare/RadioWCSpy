import rethinkdb as r
import database

class Database(database.Database):
	#class variable

	def __init__(self):
		database.Database.__init__(self, 'rethinkdb')
		#instance properties
		self.connection = None
		self.host = 'localhost'
		self.port = 28015
		self.timeout = 20
		self.database_name = 'radiowcs'
		self.auth_key = ''
		self.table_name = 'playlist'

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		if (self.connection != None):
			self.connection.close()

	def connect(self):
		"""Opens/reopens connection to the database"""
		if (self.connection != None):
			self.connection.close()
		self.connection = r.connect(
			host=self.host,
			port=self.port,
			db=self.database_name,
			auth_key=self.auth_key,
			timeout=self.timeout
		)

	def reconnect(self):
		""" Closes and reopens connection, cancels outstanding requests"""
		assert self.connection != None
		self.connection.reconnect(noreply_wait=False)

	def configure(self):
		"""Creates required database and tables/collections"""
		self.connect()
		try:
			r.db_create(self.connection.db).run(self.connection)
			r.table_create(self.table_name).run(self.connection)
			r.table(self.table_name).index_create('date')
			print 'Database setup completed.'
		except r.RqlRuntimeError:
			print 'App database already exists..'

	def insert(self, item):
		"""
			Insert an item into the database
			:param item: item being inserted
			:type item: dict
		"""
		assert self.connection != None
		assert type(self.table_name) is str
		assert type(item) is dict
		r.table(self.table_name).insert(item).run(self.connection)

	def print_inserts(self):
		"""blocking loop: prints stream of inserts"""
		assert self.connection != None
		assert type(self.table_name) is str
		rql = r.table(self.table_name).changes()
		rql = rql.filter( r.row['old_val'].eq(None) )
		for change in rql.run(self.connection):
			print change

	def latest(self):
		""" Gets the single most recent entry by 'date' """
		assert self.connection != None
		assert type(self.table_name) is str
		result = r.table(self.table_name).max('date').run(self.connection)
		# result = r.table(self.table_name).max(index='date').run(self.connection)
		return result

	def query(self, rql):
		"""
			Runs a query on this database object connection
			Create queries by importing rethinkdb. I.E. 'import rethinkdb as r'
			:param rql: A query built using rethinkdb query language (RQL)
			:return: result of query
		"""
		assert self.connection != None
		return rql.run(self.connection)

	def count(self):
		"""Returns number of entries in table"""
		assert self.connection != None
		return r.table(self.table_name).count().run(self.connection)

	def count_genres(self):
		"""
			Returns a set of genres and counts of each
			:return: json
		"""
		return r.table(self.table_name).group('genre').count().run(self.connection)

	def recent(self, qty=100, skip = 0):
		"""
			Returns most recent items
			:param qty: how many rows to return, must be less than 10000
			:type qty: int
			:param skip: how many rows to skip
			:type skip: int
			:return: json of rows in descending order by date
		"""
		assert self.connection != None
		assert qty <= 10000
		if (qty > 10000):
			qty = 10000
		idx = r.desc('date')
		return r.table(self.table_name).order_by( idx ).skip(skip).limit(qty).run(self.connection)

	@property
	def connection(self):
		"""Connection used for rql queries"""
		return self._connection
	@connection.setter
	def connection(self, value):
		"""Internal use only"""
		self._connection = value
