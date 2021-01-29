import re


def log_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
        file.close()


def check_mail(log_file, mail):
    if bool(re.search(r'^[^@]+@[^@]+\.[^@]+', mail)):
        log_to_file(log_file, 'valid mail:' + mail + '\n')
        return True
    else:
        log_to_file(log_file, 'invalid mail:' + mail + '\n')
        return False

def check_bad_mail(log_file, mail):
    if bool(re.search(r'^[^@]+@[^@]+\.[^@]+', mail)):
        log_to_file(log_file, 'valid mail:' + mail + '\n')
        return False
    else:
        log_to_file(log_file, 'invalid mail:' + mail + '\n')
        return True
