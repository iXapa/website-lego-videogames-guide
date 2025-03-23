from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


# Enum for the themes of the videogames
class Genre(enum.Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    RPG = "RPG"
    STRATEGY = "Strategy"
    PUZZLE = "Puzzle"
    SPORTS = "Sports"


# Videogame model
class Videogame(db.Model):
    id = db.Column(db.Integer, primary_key=True) # type: ignore
    name = db.Column(db.String(100), nullable=False) # type: ignore
    release_date = db.Column(db.Date, nullable=True) # type: ignore
    genre = db.Column(db.Enum(Genre), nullable=True) # type: ignore
    platform = db.Column(db.String(50), nullable=True) # type: ignore
    developer = db.Column(db.String(100), nullable=True) # type: ignore
    publisher = db.Column(db.String(100), nullable=True) # type: ignore
    description = db.Column(db.Text, nullable=True) # type: ignore
    rating = db.Column(db.Float, nullable=True) # type: ignore
    image_url = db.Column(db.String(200), nullable=True) # type: ignore


    def __repr__(self):
        return f"<Videogame {self.name} ({self.theme})>"
