import os
import pem
import logging
import binascii
import win32security
from typing import Optional
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from base64 import b64encode, b64decode

from backend.app.core.config import config
from backend.app.schemas.access import User
from backend.app.crud.active_directory import find_user

logger = logging.getLogger(__name__)


def get_user_profile(name: str) -> dict:
    return {
        'home': '',
        'groups': [],
        'routers': [],
        'favorites': {}
    }


def get_user_info(name: str) -> User:
    meta = find_user(name)

    return User(
        name=name,
        email=meta.userPrincipalName or '',
        display_name=meta.displayName or name,
        photo=b64encode(meta.thumbnailPhoto if meta.thumbnailPhoto else config.ANONYMOUS.encode('utf-8')),
        profile=get_user_profile(name)
    )


def create_security_pem():
    key = RSA.generate(2048)
    encrypted_key = key.exportKey(
        passphrase=config.SECRET_KEY,
        pkcs=8,
        protection='scryptAndAES128-CBC'
    )
    path = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(path, 'security.pem'), 'wb') as file:
        file.write(encrypted_key)


def authenticate(username: str, password: str, domain: Optional[str] = None) -> str:
    try:
        win32security.LogonUser(
            username,
            domain,
            decrypt(password),
            win32security.LOGON32_LOGON_INTERACTIVE,
            win32security.LOGON32_PROVIDER_DEFAULT
        )
    except win32security.error:
        return False
    else:
        return username


def decrypt(encrypted: str) -> str:
    path = os.path.dirname(os.path.dirname(__file__))
    certs = pem.parse_file(os.path.join(path, 'security.pem'))
    key = certs[0].sha1_hexdigest.encode('utf-8')
    try:
        encrypted = b64decode(encrypted)
    except binascii.Error:
        logger.warning('Incorrect padding')
        return encrypted
    else:
        aes = AES.new(key, AES.MODE_CBC, encrypted)
        return ''.join(i for i in aes.decrypt(encrypted).decode('utf-8') if 31 < ord(i) < 127)
