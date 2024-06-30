from flask_restful import Resource
from models import db, Artist
from flask import make_response, request

class Artists(Resource):
    def get(self):
        artists = [ artist.to_dict() for artist in Artist.query.all() ]

        return make_response(artists, 200)

    def post(self):
        new_artist = Artist(name=request.json['name'])

        db.session.add(new_artist)
        db.session.commit()

        return make_response(new_artist.to_dict(), 201)

class ArtistById(Resource):
    def get(self, id):
        artist = Artist.query.filter(Artist.id == id).first()

        return make_response(artist.to_dict(), 200)

    def patch(self, id):
        artist = Artist.query.filter(Artist.id == id).first()

        for attr in request.json:
            setattr(artist, attr, request.json[attr])

        db.session.commit()

        return make_response(artist.to_dict(), 200)

    def delete(self, id):
        artist = Artist.query.filter(Artist.id == id).first()

        db.session.delete(artist)
        db.session.commit()

        return make_response({"message": "Succesfully deleted"}, 200)