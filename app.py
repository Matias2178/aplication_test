"""
Autor: Matias Martelossi
Creation: 17/09/2022
"""
from logging import exception
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from sqlalchemy.sql.functions import current_user
from extensions import db, swagger
from dotenv import load_dotenv
from forms import PersonForm, PublicationForm
from model import Person, Publication
import os
from datetime import datetime

app = Flask(__name__)

# db Configuration load in .env file
load_dotenv()
USER_DB = os.getenv('ENV_USER_DB')
PASS_DB = os.getenv('ENV_PASS_DB')
URL_DB = os.getenv('ENV_URL_DB')
NAME_DB = os.getenv('ENV_NAME_DB')
SECRETS_KEY = os.getenv('ENV_SECRETS_KEY')

FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRETS_KEY

# db = SQLAlchemy(app)
db.init_app(app)

# Config flask migrate
migrate = Migrate()
migrate.init_app(app, db)

# Swagger initialize
swagger.init_app(app)


# USERS

@app.route('/api/registerPerson', methods=['POST'])
@swag_from('/doc/createPerson.yml')
def create_person():
    try:
        name = request.form["name"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        photo = request.form["photo"]

        person = Person(name, lastname, email, password, photo)
        db.session.add(person)
        db.session.commit()
        return jsonify(person.serialize()), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/registerPerson Log: \n")
        return jsonify({"msg": "An error has occurred"}), 500

@app.route('/api/listAllPersons', methods=['GET'])
@swag_from('/doc/listAllPersons.yml')
def list_all_persons():
    try:
        persons = Person.query.all()
        to_return = [person.serialize() for person in persons]
        return  jsonify(to_return), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/listAllPersons Log: \n")
        return jsonify({"msg": "An error has occurred"}), 500

@app.route('/api/listPerson', methods=['POST'])
@swag_from('/doc/listPerson.yml')
def list_person():
    try:
        list = {}
        if "name" in request.form["name"]:
            list["name"] = request.form["name"]

        if "lastname" in request.form["last_name"]:
            list["last_name"] = request.form["last_name"]

        if "id" in request.form["id"]:
            list["id"] = request.form["id"]

        persons = Person.query.filter_by(**list)
        to_return = [ person.serialize() for person in persons]
        return jsonify(to_return), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/listPerson. Log: \n")
        return jsonify({"msg": "An error has occurred"}), 500

# Delete person by id
@app.route('/api/delPerson', methods=['POST'])
@swag_from('/doc/delPerson.yml')
def del_person():
    try:
        id_person = request.form["id"]
        person = Person.query.filter_by(id=id_person)
        db.session.delete(person)
        db.session.commit()
        return jsonify({"msg": "Publication delete"})
    except Exception:
        exception("\n[SERVER]: Error in route /api/delPerson. Log: \n")
        return jsonify({"msg": "An error has occurred"}), 500


@app.route('/api/updatePerson', methods=['POST'])
@swag_from('/doc/updatePerson.yml')
def update_person():
    try:
        id_person = request.form["id"]
        name = request.form["name"]
        last_name = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        photo = request.form["photo"]

        person = Person()
        db.session.add(person)
        db.session.commit()
        return jsonify(person.serialize()), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/registerPerson Log: \n")
        return jsonify({"msg": "An error has occurred"}), 500

# Register a new post
@app.route('/api/createPublication', methods=["POST"])
@swag_from('/doc/createPost.yml')
def create_post():
    try:
        title = request.form["title"]
        description = request.form["description"]
        priority = request.form["priority"]
        publication = request.form["publication"]
        user = current_user
        status = 'created'
        time_published = datetime.now() - datetime.now()
        created_at = datetime.now()
        updated_at = datetime.now()
        publication = Publication(title, description, priority, status, time_published, user, created_at,
                                  updated_at, publication)

        app.logger.debug(f'Publication created: {publication}')
        db.session.add(publication)
        db.session.commit()
        return jsonify(publication.serializer()), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/createPublication Log: \n")
        return jsonify({"msg": "An error has occurred"}), 500


# Edit publication
@app.route('/api/editPublication/', methods=['POST'])
@swag_from('/doc/updatePost.yml')
def update_publication():
    try:
        id_pub = request.form["id"]
        title = request.form["title"]
        description = request.form["description"]
        priority = request.form["priority"]
        publication_text = request.form["publication"]
        publication = Publication.query.filter_by(int(id_pub)).first()
        publication_form = PublicationForm(obj=publication)

        publication_form.title = title
        publication_form.description = description
        publication_form.priority = priority
        publication_form.publication = publication_text
        publication_form.updated_at = datetime.now()
        publication_form.status = 'updated'
        app.logger.debug(f'Publication edited: {publication_form}')
        app.logger.debug(f'Save: {publication}')
        db.session.commit()
        return jsonify(publication.serializer()), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/editPublication. Log: \n")
        return jsonify({"msg": "An error has occurred"}), 500


# List Publication
@app.route('/api/listPublication', method=["GET"])
@swag_from('/doc/listPublication.yml')
def list_publication():
    try:
        publications = Publication.query.filter_by(Publication.user == current_user).all()
        for pub in publications:
            pub.time_published = datetime.now() - pub.created_at
        app.logger.debug(f'Publications: {publications}')
        to_return = [publication.serializer() for publication in publications]
        return jsonify(to_return), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/listPerson Log: \n")
        return jsonify({"msg": "An error has occurred"}), 500


# Delete Publication by id or Title
@app.route('/api/deletePublication', method=["POST"])
@swag_from('/doc/delPublication.yml')
def del_publication():
    try:
        fields = {}
        if "title" in request.args:
            fields["title"] = request.args["title"]
        if "id" in request.args:
            fields["id"] = request.args["id"]

        publication = Publication.query.filter_by(**fields).first()
        app.logger.debug(f'Publication to delete: {publication.title}')
        db.session.delete(publication)
        db.session.commit()
        return jsonify({"msg": "Publication delete"})
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "An error has occurred"}), 500


if __name__ in '__main__':
    app.run(debug=True)
