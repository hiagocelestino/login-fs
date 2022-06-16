from datetime import datetime
from flask import request,jsonify
import jwt
from werkzeug.security import check_password_hash
import datetime

def realiza_autenticacao():
    import os
    from app.models.usuarios import realiza_login
    
    login = request.json.get('login')
    senha = request.json.get('senha')
    
    usuario = realiza_login(login)

    if not usuario:
        return jsonify({'mensagem': 'Usuário não encontrado!'})

    if check_password_hash(usuario.senha, senha):
        payload = {
            'nome': usuario.nome,
            'cpf': usuario.cpf,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
        }

        token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm="HS256")

        return jsonify({'token':token, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12), 'cpf':usuario.cpf, 'nome': usuario.nome})
    
    return jsonify({'mensagem': 'Login ou Senha Incorretos!'})

