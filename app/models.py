from neomodel import StructuredNode, StringProperty, IntegerProperty, BooleanProperty, RelationshipTo, RelationshipFrom, FloatProperty

class User(StructuredNode):
    google_id = StringProperty(unique=True, required=True)
    name = StringProperty()

    tokens = RelationshipFrom("RegistrationToken", "OWNED_BY")
    uploaded_files = RelationshipFrom("File", "UPLOADED_BY")


class RegistrationToken(StructuredNode):
    __label__ = "Registration_Token"

    token = StringProperty(unique=True, required=True)
    role = StringProperty()
    id_str = StringProperty(unique=True)
    created_at = FloatProperty()
    updated_at = FloatProperty()

    user = RelationshipTo("User", "OWNED_BY")

class Project(StructuredNode):
    name = StringProperty(unique=True, required=True)
    has_files = RelationshipTo('File', "HAS_FILES")

class File(StructuredNode):
    __label__ = 'File'
    is_active = BooleanProperty(default=True)
    is_deleted = BooleanProperty(default=False)
    file_name = StringProperty(required=True)
    id_str = StringProperty(unique_index=True)
    size = IntegerProperty()
    created_at = FloatProperty()
    updated_at = FloatProperty()
    user_file_name = StringProperty()
    file_path_loc = StringProperty()

class PDFFile(File):
    __label__ = 'PDF_file'
    __labels__ = {'File'}
    pages_no = IntegerProperty()
    rasterized = BooleanProperty()

class ImageFile(File):
    __label__ = 'Image_file'
    __labels__ = {'File'}
    width = IntegerProperty()
    height = IntegerProperty()
    _is_DL_processed = BooleanProperty()
