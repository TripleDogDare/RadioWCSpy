import rethinkdb as r
import Queue
from Queue import Queue
from threading import Lock, Thread, Event

class Connection(object):
	def __init__(self):


class RethinkdbPool(object):
	def __init__(self, **kwargs):
		"""
			:param min: minimum number of connections in pool
			:type min: int
			:param max: maximum number of connections in pool
			:type max: int
			:param idleTimeout: Idle timeout for a connection in seconds, default to 1 hour
			:type idleTimeout: int
		"""
		self.min = int(kwargs.get('min', 2))
		self.max = int(kwargs.get('max',10))
		self.idleTimeout = int(kwargs.get('idleTimeout', 3600))
		self._lock = Lock()
		self._pool = Queue.Queue()

	def create(self):
		"""
			Create a connection
		"""
		pass

	def destroy(self):
		"""
			Destroy a connection
		"""
		pass

	def connection(self, timeout=30):
		self._lock.acquire()
		try:
			self._pool.get(True, timeout)
		finally:
			self._lock.release()
		return conn
		
	def query(self, rql, timeout=30):
		"""
			Run a rql query to run using this connection pool
			:param rql: a rql query
			:param timeout: time in seconds to wait for query to finish
			:type timeout: int
		"""
		return rql.run(connection(timeout))

