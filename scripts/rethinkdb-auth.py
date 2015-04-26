#!/usr/bin/python
import rethinkdb as r

new_key = 'test'
r.db_create('radiowcs').run()
r.db('radiowcs').table('cluster_config').get('auth').update({auth_key:new_key}).run()
