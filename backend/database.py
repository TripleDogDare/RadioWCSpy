class Database(object):
	"""Generic Database object"""

	def __init__(self, dbms):
		object.__init__(self)
		self._dbms = dbms

	def connect(self):
		raise NotImplementedError("Class %s doesn't implement connect()" % (self.__class__.__name__))

	def insert(self, item):
		raise NotImplementedError("Class %s doesn't implement insert()" % (self.__class__.__name__))
	
	def configure(self):
		""" Some databases might need some confguration """
		pass

	@property
	def port(self):
		return self._port
	
	@port.setter
	def port(self, value):
		if type(value) is int and value >= 0 and value < 2**16:
			self._port = value
		else:
			raise AttributeError("Class %s method port(value): value must be an integer between 0 and 65535" % (self.__class__.__name__))

	@property
	def host(self):
		return self._host
	@host.setter
	def host(self, value):
		if type(value) is str:
			self._host = value
		else:
			raise AttributeError("Class %s method host(value): value must be a string" % (self.__class__.__name__)) 
	
	@property
	def timeout(self):
		return self._timeout
	@timeout.setter
	def timeout(self, value):
		if type(value) is int and value >= 0 and value < 2**16:
			self._timeout = value
		else:
			raise AttributeError("Class %s method timeout(value): value is an integer for connection open timeout in seconds" % (self.__class__.__name__))
	
	@property
	def database_name(self):
		return self._database_name
	@database_name.setter
	def database_name(self, value):
		if type(value) is str:
			self._database_name = value
		else:
			raise AttributeError("Class %s method database_name(value): value must be a string" % (self.__class__.__name__))
	
	@property
	def auth_key(self):
		return self._auth_key
	@auth_key.setter
	def auth_key(self, value):
		if type(value) is str:
			self._auth_key = value
		else:
			raise AttributeError("Class %s method auth_key(value): value must be a string" % (self.__class__.__name__))
			
	@property
	def dbms(self):
		return self._dbms
	@dbms.setter
	def dbms(self, value):
		raise AttributeError("Class %s dbms is read-only" % (self.__class__.__name__))
		# self._dbms = value


	@property
	def table_name(self):
		return self._table_name
	@table_name.setter
	def table_name(self, value):
		if type(value) is str:
			self._table_name = value
		else:
			raise AttributeError("Class %s method table_name(value): value must be a string" % (self.__class__.__name__))
	
