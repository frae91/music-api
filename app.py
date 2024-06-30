from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, Song, Artist, Album, SongArtist
from flask_restful import Resource, Api
from controllers.songs_controller import Songs, SongById
from controllers.artists_controller import Artists, ArtistById
from controllers.albums_controller import Albums, AlbumById
from controllers.song_artists_controller import SongArtists

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return make_response({"message": "Welcome to the Music API"}, 200)

api = Api(app)

api.add_resource(Songs, "/songs")
api.add_resource(SongById, "/songs/<int:id>")
api.add_resource(Artists, "/artists")
api.add_resource(ArtistById, "/artists/<int:id>")
api.add_resource(Albums, "/albums")
api.add_resource(AlbumById, "/albums/<int:id>")
api.add_resource(SongArtists, "/song_artists")

if __name__ == "__main__":
    app.run(port=4000, debug=True)