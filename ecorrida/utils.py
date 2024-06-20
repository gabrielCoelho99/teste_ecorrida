from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Create a global SQLAlchemy instance

def initialize_db(app):
    # Bind SQLAlchemy to the app, configure database URI, etc.
    db.init_app(app)
    # Create all database tables if they don't exist
    with app.app_context():
        db.create_all()
