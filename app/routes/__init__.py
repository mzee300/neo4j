from app.routes.tokens import tokens_bp
from app.routes.projects import projects_bp
from app.routes.files import files_bp

def register_blueprints(app):
    app.register_blueprint(tokens_bp, url_prefix="/tokens")
    app.register_blueprint(projects_bp, url_prefix="/projects")
    app.register_blueprint(files_bp, url_prefix="/files")
