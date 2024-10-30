from constants import passwords_file_path, salts_file_path, default_message_text
from modules import append_salt, check_final_hash

def crack_sha1_hash(hash, use_salts = False):
    passwords_file = open(passwords_file_path, 'r')

    for sample_password in passwords_file:
        clean_password = sample_password.strip()
        is_correct_password = False

        if not use_salts:
            is_correct_password = check_final_hash(hash, clean_password)
        else:
            salts_file = open(salts_file_path, 'r')
            
            for sample_salt in salts_file:
                salted_password = append_salt(clean_password, sample_salt.strip())
                is_correct_password = check_final_hash(hash, salted_password)

                if is_correct_password:
                    break
            
            salts_file.close()

        if is_correct_password:
            return clean_password
    
    passwords_file.close()
    
    return default_message_text