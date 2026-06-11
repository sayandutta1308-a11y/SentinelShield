from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class AttackLog(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    ip_address = db.Column(
        db.String(50),
        nullable=False
    )

    attack_type = db.Column(
        db.String(100),
        nullable=False
    )

    payload = db.Column(
        db.Text,
        nullable=False
    )

    time = db.Column(
        db.DateTime,
        default=datetime.now
    )