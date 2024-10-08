from flask import Flask, jsonify, request
from models import db, Artist
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ian:ianndungu12345@localhost/music_store'

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return f"<h1>test</h1>"


@app.route('/all_artists', methods=['GET'])
def get_all_artists():
    artists = Artist.query.all()
    return jsonify([artist_item.artist_serializer() for artist_item in artists])


@app.route('/get_artist/<int:artist_id>', methods=['GET', 'DELETE'])
def get_artist(artist_id):
    artist = Artist.query.get(artist_id)

    if request.method == "GET":
        if artist is None:
            return jsonify({"message": f"Artist with id {artist_id} not found."}), 404

        return jsonify(artist.artist_serializer())
    elif request.method == "DELETE":
        db.session.delete(artist)
        db.session.commit()

        return {"message": f"artist with id {artist_id} has been deleted"}


if __name__ == "__main__":
    app.run(port=5000, debug=True)
