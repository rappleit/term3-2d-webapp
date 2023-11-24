from app import db
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash


# example of how to create association table
#association_table = db.Table('association', 
#    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'))
#)




