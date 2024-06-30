from flask_restful import Resource
from models import db, Album
from flask import make_response, request

class Albums(Resource):
    def get(self):
        albums = [ album.to_dict() for album in Album.query.all() ]

        return make_response(albums, 200)

    def post(self):
        new_album = Album(name=request.json['name'], artist_id=request.json['artist_id'])

        db.session.add(new_album)
        db.session.commit()

        return make_response(new_album.to_dict(), 201)

class AlbumById(Resource):
    def get(self, id):
        album = Album.query.filter(Album.id == id).first()

        return make_response(album.to_dict(), 200)

    def patch(self, id):
        album = Album.query.filter(Album.id == id).first()

        for attr in request.json:
            setattr(album, attr, request.json[attr])

        db.session.commit()

        return make_response(album.to_dict(), 200)

    def delete(self, id):
        album = Album.query.filter(Album.id == id).first()

        db.session.delete(album)

        return make_response({"message": "Successfully deleted"}, 200)