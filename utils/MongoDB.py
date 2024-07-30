import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Carregar variáveis do arquivo .env
load_dotenv()

# Obter a URI do MongoDB e o nome do banco de dados das variáveis de ambiente
mongo_uri = os.getenv('MONGO_URI')
database_name = os.getenv('DATABASE_NAME')

# Conectar ao MongoDB
client = MongoClient(mongo_uri)
db = client[database_name]

def list_collections():
    """Lista todas as coleções no banco de dados."""
    collections = db.list_collection_names()
    return collections

def read_collection(collection_name):
    """Lê todos os documentos de uma coleção específica e converte ObjectId para string."""
    collection = db[collection_name]
    documents = collection.find()
    result = []
    for doc in documents:
        doc['_id'] = str(doc['_id'])  # Converte ObjectId para string
        result.append(doc)
    return result

def insert_document(collection_name, document):
    """Insere um documento em uma coleção específica."""
    collection = db[collection_name]
    result = collection.insert_one(document)
    return result.inserted_id

def insert_documents(collection_name, documents):
    """Insere múltiplos documentos em uma coleção específica."""
    collection = db[collection_name]
    result = collection.insert_many(documents)
    return result.inserted_ids

def insert_collection(collection_name):
    "Insere uma nova coleção da DB"
    collection = db.create_collection(collection_name)
    result = collection.name
    return result