import jwt
import hashlib
from datetime import datetime, timedelta

SECRET_KEY = "your_super_secret_key"

# Hash password
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Verify password
def verify_password(stored: str, provided: str) -> bool:
    return stored == hash_password(provided)

# Generate JWT token
def generate_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

if __name__ == "__main__":
    users = {"user1": hash_password("pass123")}

    username = "user1"
    password = "pass123"
    if username in users and verify_password(users[username], password):
        token = generate_token(username)
        print(f"Token: {token}")
    else:
        print("Auth failed")
