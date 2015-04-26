#!/usr/bin/python

import sys, time

# import db_mongo as database
import db_rethink as database

import urllib3
import json
import copy
import traceback

recent_tracks_url	= "http://anchorstep.radiowcs.com/cast/"
http				= urllib3.PoolManager()

def get_recent_tracks():
	"""Returns the portion of the http response that contains data as json array."""
	r = http.request('GET', recent_tracks_url)
	if r.status != 200:
		raise ValueError("HTTP Error: " + r.status)
	pos_start = r.data.find('[')
	pos_end = r.data.rfind(']')
	if pos_start < 0 or pos_end < 0:
		raise ValueError("Could not parse HTTP response: " + r.data)
	data = r.data[pos_start:pos_end+1]
	if len(data) <= 0:
		raise ValueError("Parsed response is empty")
	return data

def dict_filter(d, keep):
	"""
		Remove all keys from dict except those specified in list 'keep'.
		Recurses over values to remove keys from nested dictionaries
		:param d: Dictionary from which to select key,value pairs
		:type d: dict
		:param remove: Keys to select
		:type remove: list
		:returns: dictionary with key,value pairs selected from d where key is in the keep list
	"""
	assert type(keep) is list
	if isinstance(d, dict):
		#recursively call for nested dicts
		return { key:dict_filter(value, keep) for key,value in d.iteritems() if key in keep }
	return d

def dict_exclude(d, remove):
	"""
		Remove all keys from dict specified in list 'remove'.
		Recurses over values to remove keys from nested dictionaries
		:param d: Dictionary from which to remove key,value pairs
		:type d: dict
		:param remove: Keys to remove
		:type remove: list
		:returns: passed in dict d, minus any key,value pairs where key is in the remove list
	"""
	assert type(remove) is list
	if isinstance(d, dict):
		#recursively call for nested dicts
		return {key:dict_exclude(value, remove) for key,value in d.iteritems() if key not in remove}
	return d

def main():
	"""Runs the simple web scraper parsing a jsonp response and putting the json part into a database"""
	delay = 60;#seconds
	previous_track = None
	db = database.Database()
	print "Using dbms: %s" % db.dbms
	
	#connect, we're going to let any exceptions kill the process herp derp
	db.configure()
	db.connect()

	#try to get last track added to the db
	try:
		previous_track = dict_exclude(db.latest(), ['id'])
	except Exception, e:
		pass

	while True:
		try:
			result = get_recent_tracks()
			result = json.loads(result)
			new_track = result[0]
		except Exception, e:
			print e.message
		else:
			if previous_track != new_track:
				print dict_filter(new_track, ['date','artist','title'])
				previous_track  = new_track
				try:
					db.insert(new_track)
				except Exception, e:
					print "Unable to insert track into database"
					print e.message
					print traceback.format_exc()
			else:
				print "duplicate"
		time.sleep(delay)
	#done

if __name__ == "__main__":
	#run program
	main()
