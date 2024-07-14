
from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")


class EncryptUtil:
    @staticmethod
    def hash_password(plain_password):
        return pwd_content.hash(plain_password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_content.verify(plain_password, hashed_password)
