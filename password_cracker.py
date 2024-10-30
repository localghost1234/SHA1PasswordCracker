from constants import passwords_file_lines, salts_file_lines, default_result_message
from modules import append_salt, check_final_hash

def crack_sha1_hash(hash, use_salts = False):
    for sample_password in passwords_file_lines:
        is_correct_password = False
        
        if not use_salts:
            is_correct_password = check_final_hash(hash, sample_password)
        else:
            for sample_salt in salts_file_lines:
                salted_password = append_salt(sample_password, sample_salt)
                is_correct_password = check_final_hash(hash, salted_password)

                if is_correct_password:
                    break

        if is_correct_password:
            return sample_password
            
    return default_result_message