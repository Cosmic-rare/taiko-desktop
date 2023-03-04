from flask import Blueprint, send_from_directory

static_assets = Blueprint("static_assets", __name__, static_folder="assets")

@static_assets.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(static_assets.static_folder, filename)