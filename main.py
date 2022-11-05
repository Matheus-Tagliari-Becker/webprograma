from fastapi import FastAPI, Depends, HTTPException, status, Body
from typing import Union
from sqlalchemy.orm import Session 
import crud, models, schemas 
from database import SessionLocal, get_db, engine
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer
from exceptions import FornecedorException, ClienteException, ProdutoException

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# login
@app.post("/signup", tags=["usuario"])
async def create_usuario_signup(usuario:schemas.UsuarioCreate=Body(...), db:Session= Depends(get_db)):
	try:
		crud.create_usuario(db, usuario)
		return signJWT(usuario.email)
	except UsuarioExceptio as cie:
		raise HTTPException(**cie.__dict__)

@app.post("/login", tags=["usuario"])
async def user_login(usuario: schemas.UsuarioLoginSchema= Body(...), db: Session= Depends(get_db)):
	if crud.check_usuario(db, usuario):
		return signJWT(usuario.email)
	return {"error": "E-mail ou senha incorretos!"}

#Fornecedor
#, dependencies=[Depends(JWTBearer())]
@app.post("/fornecedores", dependencies=[Depends(JWTBearer())], response_model=schemas.Fornecedor)
def create_fornecedor(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_fornecedor(db, fornecedor)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/fornecedores/{fornecedor_id}}", dependencies=[Depends(JWTBearer())], response_model=schemas.Fornecedor)
def update_usuario(fornecedor_id: int, fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_fornecedor(db, fornecedor_id, fornecedor)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/fornecedores/{fornecedor_id}", dependencies=[Depends(JWTBearer())])
def delete_fornecedor_by_id(fornecedor_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_fornecedor_by_id(db, fornecedor_id)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/fornecedores", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedFornecedor)
def get_all_usuarios(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_fornecedores = crud.get_all_fornecedores(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_fornecedores}
    return response
        
#Cliente
    
@app.post("/clientes", dependencies=[Depends(JWTBearer())], response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_cliente(db, cliente)
    except ClienteException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/clientes/{cliente_id}}", dependencies=[Depends(JWTBearer())], response_model=schemas.Cliente)
def update_cliente(cliente_id: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_cliente(db, cliente_id, cliente)
    except ClienteException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/clientes/{cliente_id}", dependencies=[Depends(JWTBearer())])
def delete_cliente_by_id(cliente_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_cliente_by_id(db, cliente_id)
    except ClienteException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/clientes", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedCliente)
def get_all_clientes(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_clientes = crud.get_all_clientes(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_clientes}
    return response
        
#Produto
    
@app.post("/produtos", dependencies=[Depends(JWTBearer())], response_model=schemas.Produto)
def create_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_produto(db, produto)
    except ProdutoException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/produtos/{produto_id}}", dependencies=[Depends(JWTBearer())], response_model=schemas.Produto)
def update_produto(produto_id: int, produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_produto(db, produto_id, produto)
    except ProdutoException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/produtos/{produto_id}", dependencies=[Depends(JWTBearer())])
def delete_produto_by_id(produto_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_produto_by_id(db, produto_id)
    except ProdutoException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/produtos", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedProduto)
def get_all_produtos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_produtos = crud.get_all_produtos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_produtos}
    return response