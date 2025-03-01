from flask import Blueprint, jsonify
from neomodel import db
from app.models import Project, PDFFile, ImageFile

files_bp = Blueprint("files", __name__)


@files_bp.route("/", methods=["GET"])
def list_project1_files():
    try:
        project = Project.nodes.get(name="Project 1")

        files = project.has_files.all()

        result = []
        for file in files:
            file_data = {
                "is_active": file.is_active,
                "is_deleted": file.is_deleted,
                "file_name": file.file_name,
                "id_str": file.id_str,
                "element_id_property": file.element_id,
            }

            if isinstance(file, PDFFile):
                file_data.update({
                    "type": "PDFFile",
                    "pages_no": file.pages_no,
                    "rasterized": file.rasterized,
                })
            elif isinstance(file, ImageFile):
                file_data.update({
                    "type": "ImageFile",
                    "width": file.width,
                    "height": file.height,
                })

            result.append(file_data)

        return jsonify(result), 200

    except Project.DoesNotExist:
        return jsonify({"error": "Project 1 not found"}), 404


@files_bp.route("/images", methods=["GET"])
def list_specific_images():
    google_id = '102718630068735143796'
    query = """
    MATCH (g:GoogleOAuth {google_id: $google_id})<-[:HAS_GOOGLE_OAUTH]-(u:User)<-[:UPLOADED_BY]-(i:Image_file)
    RETURN i;
    """
    results, _ = db.cypher_query(query, {"google_id": google_id})
    if not results:
        return jsonify({"message": "No images exist for this Google ID"}), 404

    images = []
    for row in results:
        image_node = row[0]
        image_data = {
            "file_name": image_node.get("file_name"),
            "width": image_node.get("width"),
            "height": image_node.get("height"),
            "size": image_node.get("size"),
            "id_str": image_node.get("id_str"),
            "file_path_loc": image_node.get("file_path_loc"),
            "user_file_name": image_node.get("user_file_name"),
            "created_at": image_node.get("created_at"),
            "updated_at": image_node.get("updated_at"),
            "is_active": image_node.get("is_active"),
            "is_deleted": image_node.get("is_deleted"),
            "_is_DL_processed": image_node.get("_is_DL_processed")
        }
        images.append(image_data)

    return jsonify(images), 200
