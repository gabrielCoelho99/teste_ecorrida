from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from utils import initialize_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

initialize_db(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Rota para cadastro de usuários
@app.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data.get('username')
    email = data.get('email')
    age = data.get('age')

    # Verifica se o e-mail já está cadastrado
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'E-mail já cadastrado!'}), 400

    new_user = User(username=username, email=email, age=age)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

# Rota para listar todos os usuários (apenas para debug, não deve ser exposta em produção)
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'age': user.age} for user in users]
    return jsonify(users_list), 200

if __name__ == '__main__':
    app.run(debug=True)
