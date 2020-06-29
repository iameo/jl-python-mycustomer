from flask import jsonify, request
from models.store import Store

def post():
    try:
        data = request.get_json()
        new_store = Store(**data).save()
    except Exception:
        return jsonify({'error_msg':"There was an error creating store"}), 400
    return jsonify({'added store': new_store}), 201
