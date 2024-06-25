from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"

    serialize_rules = ('-album.songs', '-song_artists.song', '-album_id')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))


    song_artists = db.relationship('SongArtist', back_populates='song', cascade='all,delete-orphan')
    artists = association_proxy('song_artists', 'artist', creator=lambda x:SongArtist(artist=x))

    def __repr__(self):
        return f"<Song {self.id}: {self.title}>"

class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    serialize_rules = ('-song_artists.artist',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    song_artists = db.relationship('SongArtist', back_populates='artist', cascade='all,delete-orphan')
    songs = association_proxy('song_artists', 'song', creator=lambda x:SongArtist(song=x))

    def __repr__(self):
        return f"<Artist {self.id}: {self.name}>"

class SongArtist(db.Model, SerializerMixin):
    __tablename__ = "song_artists"

    serialize_rules = ('-song.song_artists', '-artist.song_artists')

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    song = db.relationship('Song', back_populates='song_artists')
    artist = db.relationship('Artist', back_populates='song_artists')

    def __repr__(self):
        return f"{self.song.title} - {self.artist.name}"

class Album(db.Model, SerializerMixin):
    __tablename__ = "albums"

    serialize_rules = ('-songs.album',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    songs = db.relationship('Song', backref='album', cascade='all,delete-orphan')

    def __repr__(self):
        return f"<Album {self.id}: {self.name}>"