from app import db
from datetime import datetime
from flask_security import UserMixin, RoleMixin


class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_series = db.Column(db.String(2), nullable=False)
    card_number = db.Column(db.String(6), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    ho_bbi = db.Column(db.String(100))
    speciality = db.Column(db.String(30), nullable=False)
    university = db.Column(db.String(30), nullable=False)
    study_group = db.Column(db.String(5), nullable=False)
    start_study_year = db.Column(db.Date, nullable=False)
    end_study_year = db.Column(db.Date, nullable=False)
    thesis = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Cards %r>' % self.id


#Flask Security
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
                       )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))

