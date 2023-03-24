from pymongo import MongoClient

client = MongoClient("mongodb+srv://user_jaime:XhA7pqTDWKfQy6Nh@micluster.pns9q58.mongodb.net")
# client = MongoClient("localhost")


db = client.get_database("tesJaime")

def insertarMongo(coleccion, valor):
    col = db[coleccion]
    result = col.insert_one(valor)
    return result.inserted_id


def buscarMongo(coleccion, parametro, valor):
    col = db[coleccion]
    doc = col.find_one({parametro: valor})
    return doc

def buscarMongoAll(coleccion, parametro, valor):
    col = db[coleccion]
    docs = col.find({parametro: valor})
    return [doc for doc in docs]


def deletearMongo(coleccion, parametro, valor):
    col = db[coleccion]
    id = col.delete_one({parametro: valor})
    return id
