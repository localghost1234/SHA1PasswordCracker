from constants import passwords_file_path, salts_file_path, default_message_text
from modules import check_final_hash

def crack_sha1_hash(hash, use_salts = False):
    password_result = ''
    passwords_file = open(passwords_file_path, 'r')

    for sample_password in passwords_file:
        is_correct_password = False
        clean_password = sample_password.strip()

        if not use_salts:
            is_correct_password = check_final_hash(hash, clean_password)
        else:
            salts_file = open(salts_file_path, 'r')
            
            for sample_salt in salts_file:
                clean_salt = sample_salt.strip()
                prepended_salt = clean_salt + clean_password
                appended_salt = clean_password + clean_salt
                
                is_correct_password = check_final_hash(hash, prepended_salt) or check_final_hash(hash, appended_salt)

                if is_correct_password:
                    break
            
            salts_file.close()

        if is_correct_password:
            password_result = clean_password
            break
    
    passwords_file.close()
    
    return password_result if password_result else default_message_text