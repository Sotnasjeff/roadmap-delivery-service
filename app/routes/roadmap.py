from flask import Blueprint, request, jsonify
from app.providers.api.brasil_api import BrasilApiClient

bp = Blueprint("roadmap", __name__)

@bp.route('/roadmap/<cep>', methods=['GET'])
def getCeps(cep):
    try:
        data = BrasilApiClient.get_cep(cep)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})