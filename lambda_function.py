import json
import os
import base64

# Folder where your static files from the repo exist
STATIC_DIR = "static"

def lambda_handler(event, context):
    path = event.get("rawPath", "/")

    # default file
    if path == "/" or path == "":
        path = "/index.html"

    file_path = os.path.join(STATIC_DIR, path.lstrip("/"))

    try:
        with open(file_path, "rb") as f:
            content = f.read()

        content_type = get_content_type(file_path)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": content_type
            },
            "body": base64.b64encode(content).decode("utf-8"),
            "isBase64Encoded": True
        }

    except FileNotFoundError:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "File not found"})
        }


def get_content_type(file):
    if file.endswith(".html"):
        return "text/html"
    elif file.endswith(".css"):
        return "text/css"
    elif file.endswith(".js"):
        return "application/javascript"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".svg"):
        return "image/svg+xml"
    else:
        return "application/octet-stream"
