import hashlib

def add_salt(password, salt):
    return salt + password + salt

def check_final_hash(original_hash, sample_password):
    new_hash = hashlib.sha1(sample_password.encode('utf-8')).hexdigest()

    return original_hash == new_hash