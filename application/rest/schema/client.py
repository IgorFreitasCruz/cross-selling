from pydantic import BaseModel


class ClientSchema(BaseModel):
    """Schema validation for Client"""
    razao_social: str
    cnpj: str
    email: str
