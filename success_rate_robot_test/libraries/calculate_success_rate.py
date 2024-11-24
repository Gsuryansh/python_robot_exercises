import re
from collections import defaultdict
from datetime import datetime
import os

def check_success_rate(file_path,accepted_success_rate=20):
    log_file_path = os.path.join(os.path.dirname(__file__), '..', file_path)
    success_count = 0
    failure_count = 0

    msg3_success_pattern = re.compile(r'.*type MSG3-RRC-C-REQ status success.*')
    msg3_failure_pattern = re.compile(r'.*MSG3-UNKNOWN status timeout.*')

    with open(log_file_path, 'r') as file:
        for line in file:
            if msg3_success_pattern.match(line):
                success_count += 1
            elif msg3_failure_pattern.match(line):
                failure_count += 1
    print("Success Count:", success_count)
    print("Failure Count:", failure_count)
    total_attempts = success_count + failure_count
    success_rate = (success_count / total_attempts) * 100 if total_attempts > 0 else 0

    print(f"Overall Success Rate: {success_rate:.2f}%")
    if success_rate < accepted_success_rate:
        print("The success rate is below the accepted rate of ",accepted_success_rate)
        return False
    else:
        print("The success rate is above the accepted rate of ",accepted_success_rate)
        return True

# if __name__ == "__main__":
#     log_file_path = 'config/bs_log.txt'
#     accepted_success_rate = 20
#     parse_log_file(log_file_path,accepted_success_rate)