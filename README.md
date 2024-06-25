# Music API (Flask)

- This is a starter code for a Flask application.

---

## Setup

Run ```pipenv install``` and ```pipenv shell```

### Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy-Serializer
- Flask-RESTful

### Models & Relationships

- ```Song```, ```Artist```, ```Album```, ```SongArtist```
- ```Song``` has many ```Artist```s, through ```SongArtist```s
- ```Song``` belongs to an ```Album```
- ```Artist``` has many ```Song```s, through ```SongArtist```s
- ```Album``` has many ```Song```s