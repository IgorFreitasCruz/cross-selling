from pydantic import BaseModel


class TokenData(BaseModel):
    client_id: str | None = None

    class Config:
        extra = 'forbid'
