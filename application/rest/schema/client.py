from typing import Optional

from pydantic import BaseModel, Extra


class ClientSchema(BaseModel):
    """Schema validation for Client"""

    razao_social: str
    cnpj: str
    email: str

    class Config:
        extra = Extra.forbid


class UpdateClientSchema(BaseModel):
    """Schema validation for Client"""

    id: int
    code: Optional[str]
    razao_social: Optional[str]
    cnpj: Optional[str]
    email: Optional[str]
    ativo: Optional[bool]

    class Config:
        extra = Extra.forbid
