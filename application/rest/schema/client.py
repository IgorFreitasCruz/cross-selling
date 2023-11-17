from pydantic import BaseModel


class ClientSchema(BaseModel):
    code: str
    razao_social: str
    cnpj: str
    email: str
    ativo: str = "true"
