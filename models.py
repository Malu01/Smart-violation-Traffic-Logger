from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin # Add this
from datetime import datetime

db = SQLAlchemy()

# New User Model for Login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Violation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(20), nullable=False, index=True)
    violation_type = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    fine_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), default='Unpaid') # 'Paid' or 'Unpaid'

    def __repr__(self):
        return f'<Violation {self.vehicle_number}>'