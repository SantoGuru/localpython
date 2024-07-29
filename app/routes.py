from flask import Flask, jsonify, request
from flask_httpauth import HTTPTokenAuth
from utils.MongoDB import *

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# Exemplo de dicionário de usuários e seus tokens.
users = {
    "user1": "mysecrettoken1",
    "user2": "anothersecrettoken2"
}

@auth.verify_token
def verify_token(token):
    for user, user_token in users.items():
        if token == user_token:

            return user
    return None

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/collections', methods=['GET'])
@auth.login_required
def collections():
    collections = list_collections()
    return jsonify(collections)

@app.route('/collection/<string:collection_name>', methods=['GET'])
@auth.login_required
def get_collection(collection_name):
    documents = read_collection(collection_name)
    return jsonify(documents)

@app.route('/collection/<string:collection_name>', methods=['POST'])
@auth.login_required
def add_document(collection_name):
    document = request.json
    document_id = insert_document(collection_name, document)
    return jsonify({'inserted_id': str(document_id)})

@app.route('/collection/<string:collection_name>/bulk', methods=['POST'])
@auth.login_required
def add_documents(collection_name):
    documents = request.json
    document_ids = insert_documents(collection_name, documents)
    return jsonify({'inserted_ids': [str(doc_id) for doc_id in document_ids]})

if __name__ == '__main__':
    app.run(debug=True)
