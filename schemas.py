from datetime import date
from typing import List  
from pydantic import BaseModel

class ClienteBase(BaseModel):
    nome: str
    email: str
    fixo: str
    celular: str
    cpf: str
class ClienteCreate(ClienteBase):
    pass
class Cliente(ClienteBase):
    id: int
    class Config:
        orm_mode= True

class PaginatedCliente(BaseModel):
    limit: int
    offset: int
    data: List[Cliente]
        
class FornecedorBase(BaseModel):
    nome: str
    email: str
    fixo: str
    celular: str
    cnpj: str
class FornecedorCreate(FornecedorBase):
    pass
class Fornecedor(FornecedorBase):
    id: int
    class Config:
        orm_mode= True
        
class PaginatedFornecedor(BaseModel):
    limit: int
    offset: int
    data: List[Fornecedor]
 
class ProdutoBase(BaseModel):
    nome: str
    tipo: str
    valor: float
    quantidade: int
class ProdutoCreate(ProdutoBase):
    pass
class Produto(ProdutoBase):
    id: int
    class Config:
        orm_mode= True

class PaginatedProduto(BaseModel):
    limit: int
    offset: int
    data: List[Produto]
	
class UsuarioBase(BaseModel):
    nome: str
    email: str
class UsuarioCreate(UsuarioBase):
    senha: str
class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True
class UsuarioLoginSchema(BaseModel):
	email: str
	senha: str
	class Config:
		schema_extra= {"example": {"email": "x@x.com","senha": "pass"}}
		
class PaginatedUsuario(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]