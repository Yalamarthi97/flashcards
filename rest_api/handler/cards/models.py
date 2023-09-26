from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Identity
from datetime import datetime

db = SQLAlchemy()


class Cards(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, Identity(start=1, cycle=True), primary_key=True)
    card_value = db.Column(db.String, nullable=False)
    card_description = db.Column(db.String, nullable=False)
    bin = db.Column(db.Integer, default=0)
    up_in = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.now
    )
    wrong_choice_count = db.Column(db.Integer, default=0)
    hidden = db.Column(db.Boolean, default=False)
