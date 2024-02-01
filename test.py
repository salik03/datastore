from flask import Flask, request, jsonify
from flask_cors import CORS
from tinydb import TinyDB, Query

app = Flask(__name__)
CORS(app)

# Initialize TinyDB database
db = TinyDB('db.json')

@app.route('/api/update_profile', methods=['POST'])
def update_profile():
    try:
        data = request.get_json()
        mail = data.get('mail')
        display_name = data.get('displayName')

        # Do something with the data (e.g., store it in TinyDB)
        db.insert({'mail': mail, 'displayName': display_name})

        print(f"Received data - Mail: {mail}, Display Name: {display_name}")

        return jsonify({"success": True, "message": "Profile updated successfully"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/get_profile', methods=['GET'])
def get_profile():
    try:
        # Fetch all data from TinyDB
        profiles = db.all()

        return jsonify(profiles)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
