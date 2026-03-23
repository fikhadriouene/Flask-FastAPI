# ## Exercice 3: Gestion d'une Liste de Livres

# **Énoncé**:
# Créez une API simple pour gérer une liste de livres en mémoire.

# Routes:
# - `GET /books` - Retourner tous les livres
# - `GET /books/<id>` - Retourner un livre par ID
# - `POST /books` - Ajouter un nouveau livre

# Exemple POST:
# ```bash

# ```

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for booksz
books = [
    {"id" : 1, "title": "1984", "author": "Orwell", "year": 1949},
    {"id" : 2, "title": "Le Petit Prince", "author": "Saint-Exupéry", "year": 1943},
    {"id" : 3, "title": "L'Étranger", "author": "Camus", "year": 1942}
]

next_book_id = 4

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({
        "success": True,
        "count": len(books),
        "data": books
    }), 200

@app.route('/books/<int:book_id>', methods=['GET'])

def get_book_by_id(book_id):

    for book in books :
        if book_id == book["id"] :
            return jsonify({
                "success": True,
                "data": book
            }), 200
    
    return jsonify({
            "success": False,
            "error": "book not found",
            "book_id": book_id
        }), 404


@app.route('/books', methods=['POST'])
def create_book():

    global next_book_id

    # Check content-type
    if not request.is_json:
        return jsonify({
            "success": False,
            "error": "Request must have Content-Type: application/json"
        }), 400

    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Invalid JSON: {str(e)}"
        }), 400

    # Validate required fields
    required_fields = ['title', 'author', 'year']
    missing_fields = [f for f in required_fields if f not in data]
    if missing_fields:
        return jsonify({
            "success": False,
            "error": "Missing required fields",
            "missing": missing_fields
        }), 400

    # Create book
    new_book = {
        "id": next_book_id,
        "title": data['title'],
        "author": data['author'],
        "year": data['year'],
    }

    books.append(new_book)
    next_book_id += 1

    return jsonify({
        "success": True,
        "message": "Book created",
        "data": new_book
    }), 201




if __name__ == '__main__':
    app.run(debug=True)



