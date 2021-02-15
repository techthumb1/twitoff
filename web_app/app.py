from flask import Flask, render_template# , request
from web_app.models import DB, User


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    @app.route("/")
    def root():
        return render_template('base.html', title='home', users=User.query.all())

    return app
