from app import app
from flask import jsonify
from app.models import usuarios 
from app.decorators.token_required import token_required

@app.route('/', methods=['GET'])
@token_required
def root(usuario_atual):
    return jsonify({'message': f'Olá, {usuario_atual.nome}'})


@app.route('/auth', methods=['POST'])
def autenticacao():
    from app.utils.autenticacao import realiza_autenticacao
    return realiza_autenticacao()

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return usuarios.select_usuarios()


@app.route('/usuario', methods=['GET'])
@token_required
def get_usuario(usuario_atual):
    return jsonify(usuario_atual.to_json())


@app.route('/usuario', methods=['POST'])
def post_usuario():
    return usuarios.insert_usuario()


@app.route('/usuario', methods=['PUT'])
@token_required
def put_usuario(usuario_atual):
    return usuarios.update_usuario(usuario_atual)


@app.route('/usuario', methods=['DELETE'])
@token_required
def delete_usuario(usuario_atual):
    return usuarios.delete_usuario(usuario_atual)
