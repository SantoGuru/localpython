from flask import Flask, jsonify, request
from flask_httpauth import HTTPTokenAuth
from lib.MongoDB import list_collections, read_collection, create_collection, update_collection, delete_collection, create_documents, create_document


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

# COLLECTIONS #

# [READ] Collections -> *
@app.route('/api/collections', methods=['GET'])
@auth.login_required
def get_collections():
    collections = list_collections()
    return jsonify(collections)

# [READ] Collection -> 1
@app.route('/api/collection', methods=['GET'])
@auth.login_required
def get_collection():
    collection_name = request.args.get('collection_name')
    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400
    documents = read_collection(collection_name)
    return jsonify(documents)

# [CREATE] Collection -> 1
@app.route('/api/collection', methods=['POST'])
@auth.login_required
def add_collection():
    collection_name = request.args.get('collection_name')
    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400

    result = create_collection(collection_name)
    return jsonify({'collection_name': result})

# [UPDATE] Collection -> *
@app.route('/api/collection', methods=['PUT'])
@auth.login_required
def update_collection_data():
    collection_name = request.args.get('collection_name')
    documents = request.json
    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400

    if not documents:
        return jsonify({"error": "Missing 'documents' parameter"}), 400

    modified_count = update_collection(collection_name, documents)
    if modified_count > 0:
        return jsonify({"message": "Documents updated successfully"})
    else:
        return jsonify({"error": "No documents were updated"}), 404

# [DELETE] Collection -> 1
@app.route('/api/collection', methods=['DELETE'])
@auth.login_required
def remove_collection():
    collection_name = request.args.get('collection_name')
    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400

    delete_collection(collection_name)
    return jsonify({"message": "Collection deleted successfully"})

@app.route('/api/<string:collection_name>/document', methods=['POST'])
@auth.login_required
def add_document(collection_name):
    document = request.json

    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400

    result = create_document(collection_name, document)
    return jsonify({'inserted_id': result})

@app.route('/api/<string:collection_name>/documents', methods=['POST'])
@auth.login_required
def add_documents(collection_name):
    documents = request.json

    if not collection_name:
        return jsonify({"error": "Missing 'collection_name' parameter"}), 400

    result = create_documents(collection_name, documents)
    return jsonify({'inserted_ids': result})


if __name__ == '__main__':
    app.run(debug=True)