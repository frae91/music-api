from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, Song, Artist, Album, SongArtist
from flask_restful import Resource, Api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return make_response({"message": "Welcome to the Music API"}, 200)

api = Api(app)

if __name__ == "__main__":
    app.run(port=4000, debug=True)