import base64
import json
import re
from datetime import datetime, timedelta, timezone
from typing import Any

from Crypto.Cipher import PKCS1_OAEP
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from jose import exceptions, jwe, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app import models

from .settings import AUTHSETTINGS

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
AUTH_SECRET_KEY = AUTHSETTINGS.SECRET_KEY
AUTH_ALGORITHM = AUTHSETTINGS.ALGORITHM
AUTH_ACCESS_TOKEN_EXPIRE_MINUTES = AUTHSETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES
PUBLIC_KEY = AUTHSETTINGS.PUBLIC_KEY
PRIVATE_KEY = AUTHSETTINGS.PRIVATE_KEY


def validate_password(password: str) -> Any:
    """The result of matching the password against the regex pattern."""
    regex = re.compile(
        r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%&*._])(?!.*\s).{5,15}$"
    )
    return re.fullmatch(regex, password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """bool: True if the plain password matches the hashed password, False otherwise."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(plain_password):
    """Returns password hashed."""
    return pwd_context.hash(plain_password)


def authenticate_user(email: str, password: str, db: Session) -> models.User | bool:
    """Return user if credential validation is True."""
    if user := db.query(models.User).filter(models.User.email == email).first():  # type: ignore
        return user if verify_password(password, user.password) else False
    return False


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Returns The generated access token."""
    to_encrypt = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    # TODO encrypt expire time and decrypt correctly to decode with jwt.decode()
    to_encrypt = encrypt_data(data_dict=to_encrypt)
    to_encrypt['exp'] = expire
    return jwt.encode(to_encrypt, AUTH_SECRET_KEY, AUTH_ALGORITHM)


def encrypt_data(data_dict: dict):
    """Returns encrypted data after encoded at UTF-8"""
    encrypted_data = {}
    cipher_rsa = PKCS1_OAEP.new(PUBLIC_KEY)

    for field, value in data_dict.items():
        if isinstance(value, datetime):
            value = value.isoformat()
        encrypted_value = cipher_rsa.encrypt(value.encode("UTF-8"))
        encrypted_data[field] = base64.b64encode(encrypted_value).decode("UTF-8")

    return encrypted_data


def decrypt_data(token: str):
    """Returns decrypted data after decoded at UTF-8"""
    decrypted_data = {}
    cipher_rsa = PKCS1_OAEP.new(PRIVATE_KEY)
    # TODO IMPLEMENT
    # token_header, token_payload, token_signature = token.split(".")
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # token_payload_decoded = base64.urlsafe_b64decode(token_payload + '=' * (4 - len(token_payload) % 4))
    # token_payload_decoded_json = json.loads(token_payload_decoded)
    # for field, value in token_payload_decoded_json.items():
    #     decoded_value = base64.b64decode(value.encode("UTF-8"))
    #     decrypted_value = cipher_rsa.decrypt(decoded_value).decode("UTF-8")
    #     decrypted_data[field] = decrypted_value
    #     if field == "exp":
    #         from calendar import timegm

    #         # a = base64.b64decode(value.encode("UTF-8"))
    #         # b = cipher_rsa.decrypt(a).decode("UTF-8")
    #         decrypted_value = datetime.fromisoformat(decrypted_value) # Convierte de vuelta a datetime si es necesario
    #         decrypted_data[field] = decrypted_value.isoformat()
    #         print("hola")
    #         m = datetime.fromisoformat(decrypted_data[field])
    #         print(int(decrypted_value.timestamp()))
    #         decrypted_data[field] = int(decrypted_value.timestamp())
    # payload_dectypted = base64.urlsafe_b64encode(json.dumps(decrypted_data).encode("UTF-8")).decode("UTF-8")
    # new_token_decrypted = ".".join([token_header, payload_dectypted, token_signature])

    # print(".".join([token_header, payload_dectypted, token_signature]))
    # token_decrypted = ".".join([token_header, new_payload, token_signature])
    # print(token_decrypted)

    # for field, value in decoded_token.items():
    #     print("field", "value")
    #     print(field, value)
        # if isinstance(value, str):
        #     decoded_value = base64.b64decode(data_dict[field].encode("UTF-8"))
        #     decrypted_value = cipher_rsa.decrypt(decoded_value)
        #     decrypted_data[field] = decrypted_value.decode("UTF-8")

    return decrypted_data


def generate_token(db: Session, email: str, password: str) -> str:
    """Generate a token for a user."""
    if db_user := authenticate_user(email=email, password=password, db=db):
        access_token_expires = timedelta(minutes=AUTH_ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {
        "id": str(db_user.id),  # type: ignore
        "email": str(db_user.email)  # type: ignore
        }

        return create_access_token(data=payload, expires_delta=access_token_expires)
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='El usuario o la contraseña no coinciden',
        )


def validate_token(token: str) -> None :
    """Validates token according his generations params"""
    try:
        jwt.decode(token, AUTH_SECRET_KEY, AUTH_ALGORITHM)
    except exceptions.JWEInvalidAuth:
        return JSONResponse(
            content={"message:": "Invalid Token."},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    except exceptions.ExpiredSignatureError:
        return JSONResponse(
            content={"message:": "Token Expired"},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    except exceptions.JWTError as jwt_error:
        return JSONResponse(
            content={"message": "Unable to validate token",
                     "detail": str(jwt_error)},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
