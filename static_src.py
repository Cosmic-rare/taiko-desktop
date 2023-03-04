from flask import Blueprint, send_from_directory

static_src = Blueprint("static_src", __name__, static_folder="src")

@static_src.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(static_src.static_folder, filename)