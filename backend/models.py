from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


# Enum for the themes of the videogames
class Theme(enum.Enum):
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
    release_date = db.Column(db.Date, nullable=False) # type: ignore
    theme = db.Column(db.Enum(Theme), nullable=False) # type: ignore

    def __repr__(self):
        return f"<Videogame {self.name} ({self.theme})>"
