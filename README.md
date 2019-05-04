# Brevet Time Calculator Service

* Made to calculate open times and close times for checkpoints in a brevet. It does so using Flask to handle the page serving and mongoDB to store the data. It also offers rest APIs which can be accessed to get the open and close times in JSON or CSV format. These APIs are protected, and require a token.

The token can be viewed and assigned many ways.

The user can register and login on the frontend of the server. Upon logging in, a token will be generated and that token will remain valid for 10 minutes.
To see your token, navigate to the page at "http://0.0.0.0:5000/api/token"
To refresh the token, you must login again.

Users can also generate a token is by making a GET request via curl to "http://0.0.0.0:5000/api/token".

Example curl request:

	```
	curl -i -X POST -H "Content-Type: application/json" -d '{"username":"Nolan","password":"Pass123"}' http://127.0.0.1:5000/api/register
	```

* Register a new user:

You can user the frontend to register a new user.
Navigate to the homepage at "http://0.0.0.0:5000/" and click "register" in the top-right corner. Here you can create a new user with a username and valid password.

The username must not be taken and password must be greater than 8 chars.
The password is hashed before it is stored in the database.

Users can also make a POST request via curl or a comparable service to "http://0.0.0.0:5000/api/register".

Example curl request:

	```
	curl -u Nolan:Pass123 -i -X GET http://127.0.0.1:5000/api/token
	```

* To run the project, execute the commands "docker-compose build" and "docker-compose up" to build the docker containers and run them. Then navigate to the page at "http://0.0.0.0:5000/" in a browser.

* On the login page, a remember me button is available. Should you check this button, your user will remain logged in even if you close your browser.

* Requests made through this webservice are protected from CSRF attacks


* Available APIs: (All token protected)

	* http://0.0.0.0:5001/listAll or http://0.0.0.0:5001/listAll/json will provide both the open and close times for each checkpoint in JSON format

	* http://0.0.0.0:5001/listOpenOnly or http://0.0.0.0:5001/listOpenOnly/json will provide only the open time for each checkpoint in JSON format

	* http://0.0.0.0:5001/listCloseOnly or http://0.0.0.0:5001/listCloseOnly/json will provide only the close time for each checkpoint in JSON format

	* http://0.0.0.0:5001/listAll/csv will provide both the open and close times for each checkpoint in CSV format

	* http://0.0.0.0:5001/listOpenOnly/csv will provide only the open time for each checkpoint in CSV format

	* http://0.0.0.0:5001/listCloseOnly/csv will provide only the close time for each checkpoint in CSV format


Example curl request:

		```
		curl -u <VALID-TOKEN-HERE>: -i -X GET http://127.0.0.1:5000/listAll/csv
		```

Simply add "?top=<n>" to make the api return only the top 'n' values of the query.
	
![flask2](https://user-images.githubusercontent.com/22786772/57172765-54d3ac80-6dd9-11e9-9411-94b1508b73ae.png)
![flask1](https://user-images.githubusercontent.com/22786772/57172766-54d3ac80-6dd9-11e9-99f5-318f884b8a88.png)

