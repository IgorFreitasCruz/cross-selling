from pydantic import BaseModel, Extra


class TokenData(BaseModel):
    client_id: str | None = None

    class Config:
        extra = Extra.forbid
