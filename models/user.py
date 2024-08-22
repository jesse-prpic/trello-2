from init import db, ma
from marshmallow import fields

class User(db.Model):
    # name of the table
    __tablename__ = "users"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable = False, unique=True)
    password = db.Column(db.String, nullable = False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        cards = fields.List(fields.Nested('CardSchema', exclude=["user"]))
        fields = ("id", "name", "email", "password", "is_admin", "cards")

# to handle a single user object
user_schema = UserSchema(exclude=["password"])

# to handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])

