passwords_file_lines = open('top-10000-passwords.txt', 'r').readlines()
salts_file_lines = open('known-salts.txt', 'r').readlines()
default_result_message = 'PASSWORD NOT IN DATABASE'