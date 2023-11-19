from typing import List

from pydantic import BaseModel


class CategorySchema(BaseModel):
    """Schema validatation for category"""

    descricao: str
    dt_inclusao: str = None
    dt_alteracao: str = None
    ativo: bool = True
    client_id: int
