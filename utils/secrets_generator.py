import secrets


def generate_secret() -> str:
    secret_key = secrets.token_hex(32)
    return secret_key