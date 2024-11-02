import hashlib

def read_file(path):
    return open(path, 'r')

def check_final_hash(original_hash, password):
    new_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()

    return original_hash == new_hash