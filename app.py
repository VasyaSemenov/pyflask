from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False
db.init_app(app)


class Art(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Art %r>' % self.id


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/photo')
def photo():

    return render_template("photo.html")


@app.route('/non')
def non():
    return render_template("non.html")


if __name__ == "__main__":
    app.run(debug=True)
