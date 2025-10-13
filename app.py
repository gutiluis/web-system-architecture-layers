#!/bin/env python

from flask import Flask, request, jsonify
from services import add_user_service, list_users_service
from errors import ValidationError, DatabaseError

app = Flask(__name__)

# Global error handlers
@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({"error": str(e)}), 400

@app.errorhandler(DatabaseError)
def handle_db_error(e):
    return jsonify({"error": str(e)}), 500

@app.errorhandler(Exception)
def handle_general_error(e):
    return jsonify({"error": "Unexpected error"}), 500

# Endpoints
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    result = add_user_service(data.get("name"), data.get("email"))
    return jsonify(result), 201

@app.route("/users", methods=["GET"])
def list_users():
    users = list_users_service()
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(debug=True)
