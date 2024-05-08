import os

import dotenv
from Crypto.PublicKey import RSA


class AuthSettings:
    dotenv.load_dotenv()
    SECRET_KEY = os.getenv('AUTH_SECRET_KEY')
    ALGORITHM = os.getenv('AUTH_ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('AUTH_ACCESS_TOKEN_EXPIRE_MINUTES'))

    with open('erp_public_key.pem', 'rb') as key:
        PUBLIC_KEY = RSA.import_key(key.read())

    with open("erp_private_key.pem", "rb") as key:
        PRIVATE_KEY = RSA.import_key(key.read())
    # PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    # PUBLIC_KEY = os.getenv("PUBLIC_KEY")

AUTHSETTINGS = AuthSettings
