from app import db

class Endereco(db.Model):
    __tablename__ = 'enderecos'
    __table_args__ = {'schema':'api_flask'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pais = db.Column(db.String(150), nullable=False)
    estado = db.Column(db.String(150), nullable=False)
    municipio = db.Column(db.String(150), nullable=False)
    cep = db.Column(db.String(150), nullable=False)
    rua = db.Column(db.String(150), nullable=False)
    complemento = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.String(150), nullable=False)

    def __init__(self, pais, estado, municipio, cep, rua, numero, complemento):
        self.pais = pais
        self.estado = estado
        self.municipio = municipio
        self.cep = cep
        self.rua = rua
        self.complemento = complemento
        self.numero = numero

    def to_json(self):
        return {
            "id": self.id,
            "pais": self.pais,
            "estado": self.estado,
            "municipio": self.municipio,
            "cep": self.cep,
            "rua": self.rua,
            "complemento": self.complemento,
            "numero": self.numero
        }