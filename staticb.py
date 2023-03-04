from flask import Blueprint, send_from_directory

static_b = Blueprint("static_b", __name__, static_folder="static")

@static_b.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(static_b.static_folder, filename)