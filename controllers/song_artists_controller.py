from flask_restful import Resource
from models import db, Artist, Song, SongArtist
from flask import make_response, request

class SongArtists(Resource):
    def post(self):
        song_artist = SongArtist(artist_id=request.json['artist_id'], song_id=request.json['song_id'])

        db.session.add(song_artist)
        db.session.commit()

        return make_response({"message": "Successfully added the artist to the song"}, 201)