import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from decorators.token_required import token_required
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
host = os.environ.get("HOST")
db = os.environ.get("DATABASE")
user_db = os.environ.get("USER_DB")
pass_db = os.environ.get("PASSWORD_DB")
port = os.environ.get("PORT")
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user_db}:{pass_db}@{host}:{port}/{db}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
CORS(app)
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
@token_required
def root(usuario_atual):
    from flask import jsonify
    return jsonify({'message': f'Olá, {usuario_atual.nome}'})


@app.route('/auth', methods=['POST'])
def autenticacao():
    from utils.autenticacao import realiza_autenticacao
    return realiza_autenticacao()

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    from models import usuarios
    return usuarios.select_usuarios()


@app.route('/usuario', methods=['GET'])
@token_required
def get_usuario(usuario_atual):
    from flask import jsonify
    return jsonify(usuario_atual.to_json())


@app.route('/usuario', methods=['POST'])
def post_usuario():
    from models import usuarios
    return usuarios.insert_usuario()


@app.route('/usuario', methods=['PUT'])
@token_required
def put_usuario(usuario_atual):
    from models import usuarios
    print("aqui")
    return usuarios.update_usuario(usuario_atual)


@app.route('/usuario', methods=['DELETE'])
@token_required
def delete_usuario(usuario_atual):
    from models import usuarios
    return usuarios.delete_usuario(usuario_atual)


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0")

