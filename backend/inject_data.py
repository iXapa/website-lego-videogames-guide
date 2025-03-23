from app import app
from models import db, Videogame # type: ignore

with app.app_context():
    games = [
        "Lego Creator: Harry Potter",
        "Lego Star Wars: The Video Game",
        "Lego Star Wars II: The Original Trilogy",
        "Lego Star Wars: The Complete Saga",
        "Lego Indiana Jones: The Original Adventures",
        "Lego Batman: The Videogame",
        "Lego Rock Band",
        "Lego Indiana Jones 2: The Adventure Continues",
        "Lego Harry Potter: Years 1–4",
        "Lego Star Wars III: The Clone Wars",
        "Lego Pirates of the Caribbean: The Video Game",
        "Lego Harry Potter: Years 5–7",
        "Lego Batman 2: DC Super Heroes",
        "Lego The Lord of the Rings",
        "Lego Marvel Super Heroes",
        "The Lego Movie Videogame",
        "Lego The Hobbit",
        "Lego Batman 3: Beyond Gotham",
        "Lego Jurassic World",
        "Lego Dimensions",
        "Lego Star Wars: The Force Awakens",
        "The Lego Ninjago Movie Video Game",
        "Lego Marvel Super Heroes 2",
        "Lego The Incredibles",
        "Lego DC Super-Villains",
        "The Lego Movie 2 Videogame",
        "Lego 2K Drive",
        "Lego Star Wars: The Skywalker Saga",
        "Lego Fortnite",
        "Lego Horizon Adventures",
    ]

    for i, name in enumerate(games, start=1):
        game = Videogame(id=i, name=name)
        db.session.add(game)

    db.session.commit()

    print("Sample data added successfully.")
