from flask_sqlalchemy import SQLAlchemy
from serializers import SerializerMixin
db = SQLAlchemy()


class Music(db.Model, SerializerMixin):
    __tablename__ = 'music'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    album_audio = db.Column(db.Text)
    album_image = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artist.id'), nullable=False)

    def music_serializer(self):
        return super().serialize()

    # def music_serializer(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'album_audio': self.album_audio,
    #         'album_image': self.album_image
    #     }


class Artist(db.Model, SerializerMixin):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    musics = db.relationship('Music', backref='artist',
                             cascade="all, delete-orphan")

    def artist_serializer(self):
        artist_data = super().serialize()
        artist_data['musics'] = [music_item.music_serializer()
                                 for music_item in self.musics]
        return artist_data

    # def artist_serializer(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'location': self.location,
    #         'musics': [music_item.music_serializer() for music_item in self.musics]
    #     }
