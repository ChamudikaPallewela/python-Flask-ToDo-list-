from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Define routes
@app.route('/')  # '/' for home page
def home():
    return render_template('index.html')

# Run server
if __name__ == "__main__":
    app.run(debug=True)  # debug true for showing errors in the browser
