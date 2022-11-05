from sqlalchemy import Column, Integer, String , Float, SmallInteger, Date, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, index=True)
    nome= Column(String(150))
    email = Column(String(150), unique=True, index=True)
    fixo= Column(String(20))
    celular= Column(String(20))
    cpf= Column(String(20))
    #endereco= Column(String(20))
    
class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True, index=True)
    nome= Column(String(150))
    email = Column(String(150), unique=True, index=True)
    fixo= Column(String(20))
    celular= Column(String(20))
    cnpj= Column(String(20))
    #endereco= Column(String(20))
    
class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome= Column(String(150))
    tipo= Column(String(20))
    valor= Column(Float(20))
    quantidade= Column(Integer)