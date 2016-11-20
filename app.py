#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

functions = []

@app.route('/api/v1/functions', methods=['GET'])
def get_function():
    return jsonify({'functions': functions})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1/functions', methods=['POST'])
def create_function():
    if not request.json or not 'body' in request.json:
        abort(400)

    function = {
        'name': request.json.get('name',"foobar"),
        'body': request.json['body']
    }

    return run_function(function['body'])
    # return jsonify({'function': function}), 201

def run_function(text):
    exec(text)
    return foobar()

if __name__ == '__main__':
    app.run(debug=True)