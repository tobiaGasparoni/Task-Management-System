import jwt


class JWTProcessor():

    secret_key = 'BWx8NuXUhXW/rnIOB4HP/0GPv2I5zThHJgpc3OXrMgc='

    algorithm_name = 'HS256'

    def encode(self, payload: dict):
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm_name)

    def decode(self, token: str):
        return jwt.decode(token, self.secret_key, algorithms=self.algorithm_name)
