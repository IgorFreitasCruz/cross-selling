from datetime import datetime, timedelta

import jwt


class AuthTokenPlugin:
    secret = '1234'
    algorithm = 'HS256'
    expires = datetime.now() + timedelta(days=31)

    def __init__(self, jwt: jwt) -> None:
        self.jwt = jwt

    def create_jwt(self, data: dict) -> [str, datetime]:
        expire_date = self.expires
        data.update({'exp': expire_date})
        return (
            self.jwt.encode(data, self.secret, algorithm=self.algorithm),
            expire_date,
        )

    def decode_jwt(self, data: str) -> dict:
        return self.jwt.decode(data, self.secret, self.algorithm)


auth_token = AuthTokenPlugin(jwt)
