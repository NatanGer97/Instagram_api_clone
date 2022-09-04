from passlib.context import CryptContext

pws_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(password: str):
        return pws_cxt.hash(password)
    
    def verify(hashed_password, plain_password):
        return pws_cxt.verify(plain_password,hashed_password)
    
    