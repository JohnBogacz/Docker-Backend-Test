from website import create_app
from flask import redirect, url_for
import sys

app = create_app()

# Redirect to a default page
@app.route("/")
def root():
    return redirect(url_for('login.LOGIN_page'))
    
if __name__ == "__main__":
    app.logger.disabled = True
    sys.stdout = sys.__stdout__
    app.run(
        host='0.0.0.0',
        port=80,
        debug=True
        )
