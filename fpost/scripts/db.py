# -*- coding: utf-8 -*-
#!/usr/bin/env python

import argparse

class DataBase(object):
	"""docstring for DataBase"""

	parser = argparse.ArgumentParser(description='DataBase Operations')
	parser.add_argument('action', help='The action to take (e.g. sync, migrate, etc.)')

	def __init__(self):
		super(DataBase, self).__init__()
		args = self.parser.parse_args()
		if args.action == 'sync':
			self.db_sync()
		elif args.action == 'migrate':
			self.db_migrate()
		else:
			print self.parser.print_help()

	def db_sync(self):
		print "DataBase Sync"
		from migrate.versioning import api
		from fpost.config import SQLALCHEMY_DATABASE_URI
		from fpost.config import SQLALCHEMY_MIGRATE_REPO
		from fpost.app import db
		import os.path
		db.create_all()
		if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
		    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
		    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
		else:
		    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

	def db_migrate(self):
		print "DataBase Migrate"
		import imp
		from migrate.versioning import api
		from fpost.app import db
		from fpost.config import SQLALCHEMY_DATABASE_URI
		from fpost.config import SQLALCHEMY_MIGRATE_REPO
		migration = SQLALCHEMY_MIGRATE_REPO + '/versions/%03d_migration.py' % (api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO) + 1)
		tmp_module = imp.new_module('old_model')
		old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
		exec old_model in tmp_module.__dict__
		script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
		open(migration, "wt").write(script)
		api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
		print 'New migration saved as ' + migration
		print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))

def main():
	db = DataBase()