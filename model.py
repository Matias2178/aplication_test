"""
Autor: Matias Martelossi
Creation: 17/09/2022
"""
# Publication table
from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    photo = db.Column(db.LargeBinary())

    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Name: {self.name}, '
            f'Last_name: {self.last_name}, '
            f'Email: {self.email}'
            f'Password: {self.password}'
            f'Photo: {self.photo}'
        )

    def serialize(self):
        return{
            "Id": self.id,
            "Name": self.name,
            "Last_name": self.last_name,
            "Email": self.email,
            "Password": self.password,
            "Photo": self.photo
        }


class Publication (db.Model):
    id = db.Column(db.Integer, primay_key=True, unique=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(256))
    priority = db.Column(db.String(10))
    status = db.Column(db.String(10))
    time_published = db.Column(db.String(40))
    user = db.Column(db.String(10))
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    publication = db.Column(db.String(512))

    def __str__(self):
        return (
            f'Id: {self.id}',
            f'Title: {self.title}',
            f'Description: {self.description}',
            f'Priority: {self.priority}',
            f'Status: {self.status}',
            f'Time_published: {self.time_published}',
            f'User: {self.user}',
            f'Created_at: {self.created_at}',
            f'Updated_at: {self.updated_at}',
            f'Publication: {self.publication}'
        )

    def serializer(self):
        return {
            "Id": self.id,
            "Title": self.title,
            "Description": self.description,
            "Priority": self.priority,
            "Status": self.status,
            "Time_published": self.time_published,
            "User": self.user,
            "Created_at": self.created_at,
            "Updated_at": self.updated_at,
            "Publication": self.publication

        }

