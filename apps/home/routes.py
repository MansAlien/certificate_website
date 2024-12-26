from apps.home.home import home_get
from starlette.responses import JSONResponse

def home_register_routes(app):
    @app.get("/")
    def home():
        return home_get()

def upload_routes(app):
    @app.post("/upload")
    async def upload(request):  # Mark the function as async
        # Access the uploaded file
        form = await request.form()
        uploaded_file = form.get("file")

        if not uploaded_file:
            return JSONResponse({"error": "No file uploaded"}, status_code=400)

        # Validate file type (MIME)
        allowed_mime_types = {
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # .xlsx
            "application/vnd.ms-excel",  # .xls
            "text/csv"  # .csv
        }
        if uploaded_file.content_type not in allowed_mime_types:
            return JSONResponse({"error": "Invalid file type"}, status_code=400)

        # Validate file extension
        allowed_extensions = {".xlsx", ".xls", ".csv"}
        import os
        _, ext = os.path.splitext(uploaded_file.filename)
        if ext.lower() not in allowed_extensions:
            return JSONResponse({"error": "Invalid file extension"}, status_code=400)

        # Save the file to a directory
        file_path = f"uploads/{uploaded_file.filename}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.file.read())
        
        return JSONResponse({"message": f"File '{uploaded_file.filename}' uploaded successfully!", "path": file_path})
