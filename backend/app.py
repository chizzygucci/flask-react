from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Sample data (this could come from a database)
items = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"},
    {"id": 3, "name": "Cherry"},
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

if __name__ == '__main__':    

    app.run(host='0.0.0.0', port=5000)    




    app.run(debug=True)

