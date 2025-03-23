import os
from flask import Flask, render_template
from models import db, Videogame # type: ignore

# Get the absolute path to the frontend/templates directory
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

app = Flask(__name__, static_folder=os.path.join(frontend_dir, 'static'), template_folder=os.path.join(frontend_dir, 'templates'))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supergeheim'

db.init_app(app)

with app.app_context():
    db.create_all()  # Create the tables in the database


@app.route('/')
def index():
    # Query all videogames from the database
    lego_games = Videogame.query.all()
    return render_template('index.html', lego_games=lego_games)


if __name__ == "__main__":
    app.run(debug=True)
