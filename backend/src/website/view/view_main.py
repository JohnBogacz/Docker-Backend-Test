from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify

VIEW = Blueprint("view",
                __name__,
                url_prefix="/view",
                template_folder="templates",
                static_folder="static",
                static_url_path='/static')

@VIEW.route("/", methods=['GET', 'POST'])
def VIEW_page():
    return render_template("view.html")
