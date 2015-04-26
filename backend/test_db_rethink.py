import unittest

import logger
import db_rethink as database
import rethinkdb as r

class TestDatabase(unittest.TestCase):
	def setUp(self):
		
		self.db_name = 'radiowcs_test'
		assert self.db_name != 'radiowcs'
		self.table_name = 'test'

		self.db = database.Database()
		self.db.database_name = self.db_name
		self.db.table_name = self.table_name

		self.db.connect()

		self.connection = r.connect(
			host='localhost',
			port=28015,
			db=self.db_name,
			auth_key='',
			timeout=30
		)
		try:
			r.db_create(self.db_name).run(self.connection)
			r.table_create(self.table_name).run(self.connection)
		except r.RqlRuntimeError:
			print 'unittest setup: Drop table'
			r.table_drop(self.table_name).run(self.connection)
			r.table_create(self.table_name).run(self.connection)
		r.db(self.db_name).table(self.table_name).index_create( 'title').run(self.connection)
		r.db(self.db_name).table(self.table_name).index_create('artist').run(self.connection)
		r.db(self.db_name).table(self.table_name).index_create(  'date').run(self.connection)
		# 'out of order' insertions
		r.db(self.db_name).table(self.table_name).insert({'title':'foobar',      'artist': 'Selena',   'date': '1430183323'}).run(self.connection)
		r.db(self.db_name).table(self.table_name).insert({'title':'hello world', 'artist': 'John',     'date': '1430082566'}).run(self.connection)
		r.db(self.db_name).table(self.table_name).insert({'title':'zombie apoc', 'artist': 'xxJANExx', 'date': '1430385845'}).run(self.connection)
		r.db(self.db_name).table(self.table_name).insert({'title':'Black',       'artist': 'Kettle',   'date': '1430284300'}).run(self.connection)

	def tearDown(self):
		# try:
		# 	r.db_drop(self.db_name).run(self.connection)
		# except Exception, e:
		# 	logger.log(e)
		pass

	def test_configure(self):
		# r.table_drop(self.table_name).run(self.connection)
		r.db_drop(self.db_name).run(self.connection)
		self.db.configure()
		
		db_exists = r.db_list().contains(self.db_name).run(self.connection)
		self.assertTrue( db_exists )
		
		table_exists = r.db(self.db_name).table_list().contains(self.table_name).run(self.connection)
		self.assertTrue( table_exists )

	def test_count(self):
		self.assertEqual( self.db.count(), 4)
	
	def test_insert(self):
		date = '243008000'
		
		#count before insertion
		count = r.db(self.db_name).table(self.table_name).count().run(self.connection)
		self.assertEqual( count, 4)
		
		#select row with specific inserted time
		count = r.db(self.db_name).table(self.table_name).get_all(date, index='date').count().run(self.connection)
		self.assertEqual( count, 0)

		#insert new data
		self.db.insert({'title':'Testing 1,2,3', 'artist':'Barenaked Ladies', 'date': date})
		
		#count after insertion
		count = r.db(self.db_name).table(self.table_name).count().run(self.connection)
		self.assertEqual( count, 5)

		#select row with specific inserted time
		count = r.db(self.db_name).table(self.table_name).get_all(date, index='date').count().run(self.connection)
		self.assertEqual( count, 1)

	def test_latest(self):
		result = self.db.latest()
		self.assertEqual( result['date'], '1430085845' )

	def test_recent(self):
		middle = self.db.recent(skip=1,qty=2)
		logger.log(middle)
		self.assertEqual( len(middle), 2)
		self.assertEqual( middle[0].artist, 'John')
		self.assertEqual( middle[1].artist, 'Kettle')

if __name__ == '__main__':
    unittest.main()