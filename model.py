from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost:5432/jerry'

db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'sons'
    id = db.Column(db.Integer, primary_key=True)
    #give person model name attribute
    name = db.Column(db.String(), nullable=False)


db.create_all()


@app.route('/')
def index():
  person = Person.query.first()
  return 'Hello My Dear ' + person.name
