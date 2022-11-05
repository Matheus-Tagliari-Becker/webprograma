from sqlalchemy.orm import Session
from sqlalchemy import and_
from exceptions import ProdutoAlreadyExistError, ProdutoNotFoundError, FornecedorNotFoundError, FornecedorAlreadyExistError, ClienteNotFoundError, ClienteAlreadyExistError
import models, schemas

def check_usuario(db: Session, usuario: schemas.UsuarioLoginSchema):
	db_usuario= db.query(models.Usuario).filter(and_(models.Usuario.email== usuario.email, models.Usuario.senha== usuario.senha)).first()
	if db_usuario is None:
		return False
	return True

#Fornecedor
def create_fornecedor(db: Session, fornecedor: schemas.FornecedorCreate):
    db_fornecedor= models.Fornecedor(**fornecedor.dict())
    db.add(db_fornecedor)
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor   
    
def get_fornecedor_by_email(db: Session, fornecedor_email: str):  
    return db.query(models.Fornecedor).filter(models.Fornecedor.email== fornecedor_email).first()
    
def get_fornecedor_by_id(db: Session, fornecedor_id: int):
    db_fornecedor = db.query(models.Fornecedor).get(fornecedor_id)
    if db_fornecedor is None:
        raise FornecedorNotFoundError
    return db_fornecedor
    
def get_all_fornecedores(db: Session, offset: int, limit: int):
    return db.query(models.Fornecedor).offset(offset).limit(limit).all()
    
def update_fornecedor(db: Session, fornecedor_id: int, fornecedor: schemas.FornecedorCreate):
    db_fornecedor = get_fornecedor_by_id(db, fornecedor_id)
    db_fornecedor.nome = fornecedor.nome
    db_fornecedor.email = fornecedor.email
    db_fornecedor.fixo = fornecedor.fixo
    db_fornecedor.celular = fornecedor.celular
    db_fornecedor.cnpj = fornecedor.cnpj
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor

def delete_fornecedor_by_id(db: Session, fornecedor_id: int):
    db_fornecedor = get_fornecedor_by_id(db, fornecedor_id)
    db.delete(db_fornecedor)
    db.commit()
    return
    
#Cliente
def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente= models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_cliente_by_email(db: Session, cliente_email: str):  
    return db.query(models.Cliente).filter(models.Cliente.email== clinte_email).first()
    
def get_cliente_by_id(db: Session, cliente_id: int):
    db_cliente = db.query(models.Cliente).get(cliente_id)
    if db_cliente is None:
        raise ClienteNotFoundError
    return db_cliente
    
def get_all_clientes(db: Session, offset: int, limit: int):
    return db.query(models.Cliente).offset(offset).limit(limit).all()
    
def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteCreate):
    db_cliente = get_cliente_by_id(db, cliente_id)
    db_cliente.nome = cliente.nome
    db_cliente.email = cliente.email
    db_cliente.fixo = cliente.fixo
    db_cliente.celular = cliente.celular
    db_cliente.cpf = cliente.cpf
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente_by_id(db: Session, cliente_id: int):
    db_cliente = get_cliente_by_id(db, cliente_id)
    db.delete(db_cliente)
    db.commit()
    return
    
#Produto
def create_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto= models.Produto(**produto.dict())
    db.add(produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto
    
def get_produto_by_tipo(db: Session, produto_tipo: str):  
    return db.query(models.Produto).filter(models.Produto.tipo== produto_tipo).first()
    
def get_produto_by_id(db: Session, produto_id: int):
    db_produto = db.query(models.Produto).get(produto_id)
    if db_produto is None:
        raise ProdutoNotFoundError
    return db_produto
    
def get_all_produtos(db: Session, offset: int, limit: int):
    return db.query(models.Produto).offset(offset).limit(limit).all()
    
def update_produto(db: Session, produto_id: int, produto: schemas.ProdutoCreate):
    db_produto = get_produto_by_id(db, produto_id)
    db_produto.nome = produto.nome
    db_produto.tipo = produto.tipo
    db_produto.valor = produto.valor
    db_produto.quantidade = produto.quantidade
    db.commit()
    db.refresh(db_produto)
    return db_produto

def delete_produto_by_id(db: Session, produto_id: int):
    db_produto = get_produto_by_id(db, produto_id)
    db.delete(db_produto)
    db.commit()
    return