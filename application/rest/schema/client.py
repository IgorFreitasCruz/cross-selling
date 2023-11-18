from pydantic import BaseModel


class ClientSchema(BaseModel):
    """Schema validation for Client"""
    code: str
    razao_social: str
    cnpj: str
    email: str
    ativo: str = "true"
