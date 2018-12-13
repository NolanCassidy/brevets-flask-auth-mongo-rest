from pymongo import MongoClient
import pymongo
from flask import Flask, request, render_template, jsonify, redirect, url_for, abort
from flask_restful import Resource, Api
from psw import hash_password, verify_password
from createToken import generate_auth_token, verify_auth_token

app = Flask(__name__)
api = Api(app)

client = MongoClient('db', 27017)
db = client.tododb
userdb = client.users

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'

@app.route('/api/register')
def register():
	_items = userdb.users.find()
	items = [item for item in _items]
	return render_template('register.html')

@app.route('/api/token')
def login():
	return render_template('login.html')

@app.route('/user', methods=['POST'])
def user():
	username = request.form['username']
	password = request.form['password']

	if username is None or password is None:
		return render_template("400.html"), 400

	if userdb.users.find_one({'username': username}) != None:
		return render_template("401.html"), 401

	pswd = hash_password(password)
	userdb.users.insert_one({ 'username':username, 'password':pswd })

	_items = userdb.users.find()
	items = [item for item in _items]
	user = userdb.users.find_one({ 'username':username, 'password':pswd })

	return jsonify(result={'username': username, 'password': pswd, '_id': str(user['_id'])}), 201

@app.route('/makeToken', methods=['POST'])
def makeToken():
	username = request.form['username']
	password = request.form['password']

	if username is None or password is None:
		return render_template("400.html"), 400

	if userdb.users.find_one({'username':username})==None:
		return render_template("401.html"), 401

	user = userdb.users.find_one({'username':username})

	if verify_password(password,user['password'])==False:
		return render_template("401.html"), 401

	token = generate_auth_token(app.config['SECRET_KEY'],{'id':str(user['_id'])})
	return jsonify(result={'token':str(token) ,'duration':30}), 201

class listAll(Resource):
	def get(self):
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
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
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
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
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
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
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
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
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
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
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
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
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
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
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
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
		token = request.args.get('token')
		if token == None: # makes sure a token was entered
			return render_template("401.html"), 401

		verified = verify_auth_token(token,app.config['SECRET_KEY'])
		if verified == False:
			return render_template("401.html"), 401

		if verified == True:
			top = int(request.args.get('top')) if request.args.get('top') else 20

			_items = db.tododb.find()
			_items = _items.sort([('otime',pymongo.ASCENDING), ('ctime',pymongo.ASCENDING)]).limit(top)
			items = [item for item in _items]

			csv = ""
			for item in items:
				csv += item['ctime'] + ", "

			return csv[:-2]


api.add_resource(listAll, '/listAll')
api.add_resource(listAlljson, '/listAll/json')
api.add_resource(listAllcsv, '/listAll/csv')

api.add_resource(listOpen, '/listOpenOnly')
api.add_resource(listOpenjson, '/listOpenOnly/json')
api.add_resource(listOpencsv, '/listOpenOnly/csv')

api.add_resource(listClose, '/listCloseOnly')
api.add_resource(listClosejson, '/listCloseOnly/json')
api.add_resource(listClosecsv, '/listCloseOnly/csv')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
