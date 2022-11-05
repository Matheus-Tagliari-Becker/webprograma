class FornecedorException(Exception):
    ...

class FornecedorNotFoundError(FornecedorException):
    def __init__(self):
        self.status_code = 404
        self.detail = "FORNECEDOR_NAO_ENCONTRADO"


class FornecedorAlreadyExistError(FornecedorException):
    def __init__(self):
        self.status_code = 409
        self.detail = "FORNECEDOR_DUPLICADO"
        
class ClienteException(Exception):
    ...

class ClienteNotFoundError(ClienteException):
    def __init__(self):
        self.status_code = 404
        self.detail = "CLIENTE_NAO_ENCONTRADO"


class ClienteAlreadyExistError(ClienteException):
    def __init__(self):
        self.status_code = 409
        self.detail = "CLIENTE_DUPLICADO"

class ProdutoException(Exception):
    ...

class ProdutoNotFoundError(ProdutoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "PRODUTO_NAO_ENCONTRADO"


class ProdutoAlreadyExistError(ProdutoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "PRODUTO_DUPLICADO"