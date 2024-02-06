from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from flask_cors import cross_origin

UPLOAD = Blueprint("upload",
                __name__,
                url_prefix="/upload",
                template_folder="templates",
                static_folder="static",
                static_url_path='/static')

@UPLOAD.route("/", methods=['GET', 'POST'])
def UPLOAD_page():
    return render_template("upload.html")
