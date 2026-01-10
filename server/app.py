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
    pass

@app.route('/episodes/<int:id>')
def get_episodes_id(id):
    pass


@app.route('/guests')
def get_guests():
    pass


@app.route('/appearances', methods=['POST'])
def create_appearance():
    pass



if __name__ == '__main__':
    app.run(port=5555, debug=True)