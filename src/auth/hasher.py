import hashlib


class Hasher():

    hashing_encoding = 'UTF-8'

    def hash_password(self, raw_pwd):
        hasher = hashlib.sha256()
        hasher.update(f"{raw_pwd}".encode(encoding=self.hashing_encoding))
        hashed_password = hasher.hexdigest()
        return hashed_password