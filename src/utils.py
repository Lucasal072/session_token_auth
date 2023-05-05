from base64 import urlsafe_b64decode, urlsafe_b64encode
from typing import Union


def encodebase64url(data: str) -> bytes:
    return urlsafe_b64encode(data.encode())

def decodebase64url(data: str) -> Union[bytes,None]:
    try:
        decoded_data = urlsafe_b64decode(data.encode())
    except:
        return None
    return decoded_data