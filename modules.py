from constants import sha1_hash

def hash_password(sample_password):
    return sha1_hash(sample_password).hexdigest()

def append_salt(password, salt):
    return salt + password + salt

def check_final_hash(original_hash, password):
    return original_hash == hash_password(password)