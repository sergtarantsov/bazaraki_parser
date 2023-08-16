import time

def log_record_expire(link, log_file):
    with open(log_file, 'a') as file:
        file.write(f"{'Expire'}, {time.ctime()}, {link}\n")
    file.close()