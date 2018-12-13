from pymongo import MongoClient
import pymongo
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

client = MongoClient('db', 27017)
db = client.tododb

class listAll(Resource):
	def get(self):
		times = {}

		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)])
		items = [item for item in _items]

		olist = []
		for item in items:
			olist.append(item['otime'])
		times['otime'] = olist

		clist = []
		for item in items:
			clist.append(item['ctime'])
		times['ctime'] = clist

		return times

class listAlljson(Resource):
	def get(self):
		times = {}

		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)])
		items = [item for item in _items]

		olist = []
		for item in items:
			olist.append(item['otime'])
		times['otime'] = olist

		clist = []
		for item in items:
			clist.append(item['ctime'])
		times['ctime'] = clist

		return times

class listAllcsv(Resource):
	def get(self):
		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)])
		items = [item for item in _items]

		csv = ""
		for item in items:
			csv += item['otime'] + ", "
			csv += item['ctime'] + ", "

		return csv[:-2]

class listOpen(Resource):
	def get(self):
		times = {}
		top = int(request.args.get('top')) if request.args.get('top') else 20

		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)]).limit(top)
		items = [item for item in _items]

		olist = []
		for item in items:
			olist.append(item['otime'])
		times['otime'] = olist

		return times

class listOpenjson(Resource):
	def get(self):
		times = {}
		top = int(request.args.get('top')) if request.args.get('top') else 20

		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)]).limit(top)
		items = [item for item in _items]

		olist = []
		for item in items:
			olist.append(item['otime'])
		times['otime'] = olist

		return times

class listOpencsv(Resource):
	def get(self):
		top = int(request.args.get('top')) if request.args.get('top') else 20

		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)]).limit(top)
		items = [item for item in _items]

		csv = ""
		for item in items:
			csv += item['otime'] + ", "

		return csv[:-2]

class listClose(Resource):
	def get(self):
		times = {}
		top = int(request.args.get('top')) if request.args.get('top') else 20

		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)]).limit(top)
		items = [item for item in _items]

		clist = []
		for item in items:
			clist.append(item['ctime'])
		times['ctime'] = clist

		return times

class listClosejson(Resource):
	def get(self):
		times = {}
		top = int(request.args.get('top')) if request.args.get('top') else 20

		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)]).limit(top)
		items = [item for item in _items]

		clist = []
		for item in items:
			clist.append(item['ctime'])
		times['ctime'] = clist

		return times

class listClosecsv(Resource):
	def get(self):
		top = int(request.args.get('top')) if request.args.get('top') else 20

		_items = db.tododb.find()
		_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)]).limit(top)
		items = [item for item in _items]

		csv = ""
		for item in items:
			csv += item['ctime'] + ", "

		return csv[:-2]

class Laptop(Resource):
    def get(self):
        return {
            'Laptops': ['Mac OS', 'Dell',
            'Windozzee',
	    'Yet another laptop!',
	    'Yet yet another laptop!'
            ]
        }

api.add_resource(listAll, '/listAll')
api.add_resource(listAlljson, '/listAll/json')
api.add_resource(listAllcsv, '/listAll/csv')

api.add_resource(listOpen, '/listOpenOnly')
api.add_resource(listOpenjson, '/listOpenOnly/json')
api.add_resource(listOpencsv, '/listOpenOnly/csv')

api.add_resource(listClose, '/listCloseOnly')
api.add_resource(listClosejson, '/listCloseOnly/json')
api.add_resource(listClosecsv, '/listCloseOnly/csv')

api.add_resource(Laptop, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
