from flask import Blueprint, jsonify
from app.models import Project

projects_bp = Blueprint("projects", __name__)

@projects_bp.route("/", methods=["GET"])
def list_projects():
    projects = Project.nodes.all()
    return jsonify([{"name": project.name} for project in projects])
