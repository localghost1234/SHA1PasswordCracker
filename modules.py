import hashlib

def hash_password(sample_password):
    return hashlib.sha1(sample_password.encode('utf-8')).hexdigest()

def add_salt(password, salt):
    return salt + password + salt

def check_final_hash(original_hash, password):
    return original_hash == hash_password(password)