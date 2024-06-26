
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
    bcrypt.init_app(app)

    # class User (db.Model):
    #
    #     __tablename__ = "users"
    #
    #
    # @classmethod
    # def register(cls, username, pwd):
    #     """Register user w/hashed password & return user"""
    #
    #     hashed = bcrypt.generate_password_hash(pwd)
    #     #turn bytestring into normal (unicode utf8) string
    #
    #     hashed_utf8 = hashed.decode("utf8")
    #
    #     #return instance of user w/username and hashed pwd
    #     return cls(username=username, password=hashed_utf8)

# @classmethod
# def authenticate(cls, username, pwd):
#     """Validate that user exists&password is correct.
#     Return user if valid; else return False.
#     """
#     u = User.query.filter_by(username=username).first()
#
#     if u and bcrypt.check_password_hash(u.password, pwd):
#         #return user instanse
#         return u
#     else:
#         return False