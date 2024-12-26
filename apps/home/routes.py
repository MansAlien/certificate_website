import os
from datetime import date

from fasthtml.common import RedirectResponse, database

from apps.home.home import home_get
from db_setup import conference

UPLOAD_DIR = 'uploads'

def home_register_routes(app):
    @app.get("/")
    def home():
        return home_get(conference())

def upload_routes(app):
    @app.post("/upload")
    async def upload(request):
        # Access the uploaded file
        form = await request.form()
        uploaded_file = form.get("file")

        if not uploaded_file:
            return "No file uploaded", 400

        # Validate file type (MIME)
        allowed_mime_types = {
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # .xlsx
            "application/vnd.ms-excel",  # .xls
            "text/csv"  # .csv
        }
        if uploaded_file.content_type not in allowed_mime_types:
            return "Invalid file type", 400

        # Validate file extension
        allowed_extensions = {".xlsx", ".xls", ".csv"}
        _, ext = os.path.splitext(uploaded_file.filename)
        if ext.lower() not in allowed_extensions:
            return "Invalid file extension", 400

        # Save the file to the uploads directory
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.filename)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.file.read())

        # Extract conference name from file name
        conference_name = os.path.splitext(uploaded_file.filename)[0]

        # Save to database
        conference.insert(dict(
            name=conference_name,
            date=date.today().isoformat(),
            path=file_path  # Save the file path
        ))

        # Redirect to the home page or a success page
        return RedirectResponse("/", status_code=303)
