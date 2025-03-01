from flask import Blueprint, jsonify
from app.models import RegistrationToken

tokens_bp = Blueprint("tokens", __name__)

@tokens_bp.route("/", methods=["GET"])
def list_tokens():
    tokens = RegistrationToken.nodes.all()
    return jsonify([{"value": token.token} for token in tokens])
