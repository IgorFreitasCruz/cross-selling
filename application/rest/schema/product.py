from pydantic import BaseModel


class ProductSchema(BaseModel):
    """Schema validatation for product"""
    nome: str
    descricao: str
    sku: str
    categoria_id: int
