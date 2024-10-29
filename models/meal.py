from database import db
from datetime import datetime, timezone

class Meal(db.Model):
    __tablename__ = 'meals'  # Nome da tabela no banco de dados
    
    # Definição das colunas
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    name = db.Column(db.String(100), nullable=False)  # Nome obrigatório
    description = db.Column(db.String(255), nullable=True)  # Descrição opcional
    date = db.Column(db.String(10), nullable=False) # Data
    hour = db.Column(db.String(5), nullable=False)
    inside_diet = db.Column(db.Boolean, nullable=True, default=False)  # Booleano obrigatório

    # Construtor da classe
    def __init__(self, name, date, hour, description=None, inside_diet=False):
        self.name = name
        self.description = description
        self.date = date
        self.hour = hour
        self.inside_diet = inside_diet