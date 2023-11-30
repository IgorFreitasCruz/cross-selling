from pydantic import BaseModel, Extra


class TransactionSchema(BaseModel):
    """Schema validatation for transaction"""

    client_id: int
    produto_id: int
    quantidade: int

    class Config:
        extra = Extra.forbid
