from cryptography.fernet import Fernet
import base64

def get_key(password: str) -> bytes:
    # Convert password to bytes and pad/truncate to 32 bytes
    key = password.encode('utf-8')
    key = key + b' ' * (32 - len(key)) if len(key) < 32 else key[:32]
    return base64.urlsafe_b64encode(key)

def encrypt_text(text: str, password: str) -> str:
    f = Fernet(get_key(password))
    return f.encrypt(text.encode()).decode()

def decrypt_text(encrypted_text: str, password: str) -> str:
    f = Fernet(get_key(password))
    return f.decrypt(encrypted_text.encode()).decode()