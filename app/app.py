"""This is a simple Flask application to demonstrate basic routing and rendering templates."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    """Route for the homepage."""
    return "Hello CPS3500!"

@app.route("/new_page")
def new_page():
    """Route for the new page."""
    return "This is a New Page!"

@app.route("/render_template")
def display():
    """Route to render the template."""
    return render_template("templates.html")

@app.route("/user/<username>")
def user(username):
    """Route for verifying user and rendering template with a username."""
    return render_template("templates.html", username=username)

# Run the Flask app in debug mode if this file is the main module
if __name__ == "__main__":
    app.run(debug=True)
