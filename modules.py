import hashlib

def hash_password(sample_password):
    return hashlib.sha1(sample_password.encode('utf-8')).hexdigest()

def append_salt(password, salt):
    salted_password_recipient = []
    salted_password_recipient.append(salt)
    salted_password_recipient.append(password)
    salted_password_recipient.append(salt)

    return ''.join(salted_password_recipient)

def check_final_hash(original_hash, password):
    return original_hash == hash_password(password)