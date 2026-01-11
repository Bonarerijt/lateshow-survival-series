from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Episode, Appearance, Guest

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lateshow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Welcome to lateshow survival series!</h1>'


@app.route('/episodes')
def get_episodes():
    episodes = [episode.to_dict() for episode in Episode.query.all()]
    return make_response(episodes, 200)


@app.route('/episodes/<int:id>')
def get_episode_id(id):
    episode = Episode.query.filter_by(id=id).first()

    if not episode:
        return make_response({"error": "Episode not found"}, 404)
    
    episode_dict = episode.to_dict()
    return make_response(episode_dict, 200)


@app.route('/guests')
def get_guests():
    guests = [guest.to_dict() for guest in Guest.query.all()]
    return make_response(guests, 200)


@app.route('/appearances', methods=['POST'])
def create_appearance():
    new_appearance = Appearance(
        rating= request.form.get('rating'),
        guest_id= request.form.get('guest_id'),
        episode_id= request.form.get('episode_id'),
    )

    db.session.add(new_appearance)
    db.session.commit()

    new_appearance_dict= new_appearance.to_dict
    return make_response(new_appearance_dict, 201)



if __name__ == '__main__':
    app.run(port=5555, debug=True)