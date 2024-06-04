from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bookdb"
mongo = PyMongo(app)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    result = mongo.db.books.insert_one(data)
    return jsonify(str(result.inserted_id)), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = mongo.db.books.find()
    return jsonify([book for book in books])

@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = mongo.db.books.find_one({"_id": ObjectId(id)})
    return jsonify(book)

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    mongo.db.books.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Book updated"})

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    mongo.db.books.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Book deleted"})

if __name__ == '__main__':
    app.run(port=3000)
