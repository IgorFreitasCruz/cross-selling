from typing import Optional

from pydantic import BaseModel, Extra


class CategorySchema(BaseModel):
    """Schema validatation for category"""

    descricao: str
    dt_inclusao: str = None
    dt_alteracao: str = None
    ativo: bool = True
    client_id: int

    class Config:
        extra = Extra.forbid


class UpdateCategorySchema(BaseModel):
    """Schema validatation for upadting a category"""

    id: int
    code: Optional[str]
    descricao: Optional[str]
    ativo: Optional[bool]

    class Config:
        extra = Extra.forbid
