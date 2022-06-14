from datetime import datetime
from flask import request,jsonify
import jwt
from werkzeug.security import check_password_hash
import datetime

def realiza_autenticacao():
    import os
    from decorators.token_required import usuario_por_nome
    
    dados = request.get_json('login')
    login = dados.get('login')
    senha = dados.get('senha')
    
    usuario = usuario_por_nome(login)

    if not usuario:
        return jsonify({'mensagem': 'Usuário não encontrado!'})

    if check_password_hash(usuario.senha, senha):
        payload = {
            'nome': usuario.nome,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
        }

        token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm="HS256")

        return jsonify({'token':token, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12), 'id':usuario.id, 'nome': usuario.nome})
    
    return jsonify({'mensagem': 'Login ou Senha Incorretos!'})

