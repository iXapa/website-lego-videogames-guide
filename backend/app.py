from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# Importing models after db initialization to avoid circular imports
from models import Videogame

# Initialize Flask app and database
app = Flask(__name__, static_folder="../frontend/static", template_folder="../frontend/templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supergeheim'

db = SQLAlchemy(app)


@app.route('/')
def index():
    # Query all videogames from the database
    videogames = Videogame.query.all()
    return render_template('index.html', videogames=videogames)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the tables in the database
    app.run(debug=True)
