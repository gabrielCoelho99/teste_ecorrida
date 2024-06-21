from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from models import create_user_model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


User = create_user_model()


@app.before_first_request
def create_tables():
    db.create_all()

# Rota para o formulário de cadastro (GET)
@app.route('/cadastro')
def cadastro_form():
    return render_template('cadastro.html')

# Rota para registrar um novo usuário (POST)
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    age = data.get('age')
    password = data.get('password')

    # Verifica se o e-mail já está cadastrado
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'E-mail já cadastrado!'}), 400

    # Gera o hash da senha
    hashed_password = generate_password_hash(password, method='sha256')

    # Cria um novo usuário no banco de dados
    new_user = User(username=username, email=email, age=age, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

# Rota para listar todos os usuários (GET)
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'age': user.age} for user in users]
    return jsonify(users_list), 200

if __name__ == '__main__':
    app.run(debug=True)

