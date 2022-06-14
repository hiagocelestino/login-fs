from functools import wraps
import jwt
from flask import request, jsonify
import os

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None
        if 'authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'mensagem': 'Necessário token de autenticação!'}), 401

        try:
            data = jwt.decode(token, os.environ.get("SECRET_KEY"), algorithms=["HS256"])
            usuario_atual = usuario_por_nome(nome_usuario=data['nome'])

        except:
            return jsonify({'mensagem': 'Token invalido ou expirado!'}), 401

        return f(usuario_atual, *args, **kwargs)

    return decorated


def usuario_por_nome(nome_usuario):
    from models.usuarios import Usuario
    try:
        return Usuario.query.filter(Usuario.nome == nome_usuario).one()
    except:
        return None