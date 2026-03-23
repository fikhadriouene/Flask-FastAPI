from flask import Flask, jsonify

app = Flask(__name__)


message_db = {
    "english": "Hello!",
    "french": "Bonjour!"
}

@app.route('/hello/<language>', methods=['GET'])
def get_message(language):
    if language not in message_db:
        return jsonify({
            "success": False,
            "error": f"Language '{language}' not supported"
        }), 404

    return jsonify({
        "message": message_db[language],
        "language": language
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)