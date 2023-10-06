from passlib.context import CryptContext

# bcrypt init
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# class to manage hashing of password and verify it
class HashPassword:

    # hashes password and returns it
    def create_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    # verifies password and hashed password
    def verify_hash(self, plain_pwd, hash_pwd) -> bool:
        try:
            return pwd_context.verify(secret=plain_pwd, hash=hash_pwd)
        except:
            # for invalid hashed password pass
            return False
