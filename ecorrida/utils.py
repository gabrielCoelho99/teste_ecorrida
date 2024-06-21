from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_db(app):
    db.init_app(app)
    # Não é necessário criar as tabelas aqui, será feito no app.py
