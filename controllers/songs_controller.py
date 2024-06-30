from flask_restful import Resource
from models import db, Song
from flask import make_response, request

class Songs(Resource):
    def get(self):
        songs = [ song.to_dict() for song in Song.query.all() ]

        return make_response(songs, 200)

    def post(self):
        new_song = Song(title=request.json['title'], duration=request.json['duration'], album_id=request.json['album_id'])

        db.session.add(new_song)
        db.session.commit()

        return make_response(new_song.to_dict(), 201)

class SongById(Resource):
    def get(self, id):
        song = Song.query.filter(Song.id == id).first()

        return make_response(song.to_dict(), 200)

    def patch(self, id):
        song = Song.query.filter(Song.id == id).first()

        for attr in request.json:
            setattr(song, attr, request.json[attr])

        db.session.commit()

        return make_response(song.to_dict(), 200)

    def delete(self, id):
        song = Song.query.filter(Song.id == id).first()

        db.session.delete(song)
        db.session.commit()

        return make_response({"message": "Successfully deleted"}, 200)