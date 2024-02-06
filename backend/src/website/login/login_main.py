from flask import Blueprint, render_template, request, redirect, url_for, session, flash

LOGIN = Blueprint("login",
                __name__,
                url_prefix='/login',
                template_folder="templates",
                static_folder="static",
                static_url_path='/login/static')

@LOGIN.route("/", methods=['GET', 'POST'])
def LOGIN_page():
    return render_template("login.html")



