import hashlib

def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    print(f"Hashed : {hashed}")
    print(f"Original : {password}")
hash_password("securepassword1234")
hash_password("catdog")