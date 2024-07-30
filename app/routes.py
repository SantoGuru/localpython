from flask import Flask, jsonify, request
from flask_httpauth import HTTPTokenAuth
from lib.MongoDB import *

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

# /collections 1 -> *
# [READ]
@app.route('/api/collections', methods=['GET'])
@auth.login_required
def collections():
    collections = list_collections()
    return jsonify(collections)

# /api/collection
# [READ]
@app.route('/api/collection', methods=['GET'])
@auth.login_required
def read_collection():
    collection_name = request.args.get('collection_name')
    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400

    documents = read_collection(collection_name)
    return jsonify(documents)

# [CREATE]
@app.route('/api/collection', methods=['POST'])
@auth.login_required
def create_collection():
    collection_name = request.args.get('collection_name')
    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400
    document_id = create_collection(collection_name)
    return jsonify({'inserted_collection': str(document_id)})

# [UPDATE]
@app.route('/api/collection', methods=['PUT'])
@auth.login_required
def update_collection():
    collection_name = request.args.get('collection_name')
    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400
    
    document_id = create_collection(collection_name)
    return jsonify({'inserted_collection': str(document_id)})

# [DELETE]

# /collection ?NAME 1 -> *
@app.route('/collection/<string:collection_name>/bulk', methods=['POST'])
@auth.login_required
def add_documents(collection_name):
    documents = request.json
    document_ids = create_documents(collection_name, documents)
    return jsonify({'inserted_ids': [str(doc_id) for doc_id in document_ids]})

if __name__ == '__main__':
    app.run(debug=True)
