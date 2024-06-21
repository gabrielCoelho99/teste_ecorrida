# models.py
def create_user_model(db):
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), nullable=False)
        email = db.Column(db.String(120), nullable=False)
        age = db.Column(db.Integer, nullable=False)
    return User
