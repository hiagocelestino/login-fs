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
    return jsonify({'message': 'Hello world!'})


@app.route('/auth', methods=['POST'])
def autenticacao():
    from utils.autenticacao import realiza_autenticacao
    return realiza_autenticacao()

@app.route('/usuario', methods=['GET'])
def get_usuarios():
    from models import usuarios
    return usuarios.select_usuarios()


@app.route('/usuario/<id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    from models import usuarios
    return usuarios.select_usuario(id_usuario)


@app.route('/usuario', methods=['POST'])
def post_usuario():
    from models import usuarios
    return usuarios.insert_usuario()


@app.route('/usuario/<id_usuario>', methods=['PUT'])
def put_usuario(id_usuario):
    from models import usuarios
    return usuarios.update_usuario(id_usuario)


@app.route('/usuario/<id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    from models import usuarios
    return usuarios.delete_usuario(id_usuario)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

