import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS

def create_app(test_config=None):
	# create and configure app
	app = Flask(__name__)

	# Settings up CORS. Allow '*' for origins
	CORS(app, resource={r'/api/*': {'origin': '*'}})

	@app.after_request
	def after_request(response):
		response.headers.add('Access-Control-Allow-Headers', 'Context-Type, Authorization, True')
		response.headers.add('Access-Control-Allow-Methods', 'GET')

		return response

	@app.route('/', methods=['GET'])
	def home():

		return jsonify({
			'slackUsername': 'Emmanuel Olagoke',
			'backend': True,
			'age': 24,
			'bio': "I'm a graduate of Eletronic and Electrical Engineering, from OAU, Ile-Ife. I have interest in backend technologies"
			})

	return app


if __name__ == '__main__':
	app = create_app()
	app.run(debug=False, host='0.0.0.0')