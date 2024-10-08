from models import Music, Artist, db
from app import app

with app.app_context():
    artist1 = Artist(name="artist one", location="artist one locale")
    artist2 = Artist(name="artist two", location="artist two locale")

    music1 = Music(title="music one", album_audio="musiconelink",
                   album_image="musiconelink", artist=artist1)
    music2 = Music(title="music two", album_audio="musictwolink",
                   album_image="musictwolink", artist=artist1)
    music3 = Music(title="music three", album_audio="musicthreelink",
                   album_image="musicthreelink", artist=artist2)

    db.session.add(artist1)
    db.session.add(artist2)
    db.session.add(music1)
    db.session.add(music2)
    db.session.add(music3)

    db.session.commit()
