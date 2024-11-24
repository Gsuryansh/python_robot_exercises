import re
from collections import defaultdict
from datetime import datetime

def parse_log_file(file_path):
    success_count = 0
    failure_count = 0
    hourly_stats = defaultdict(lambda: {'success': 0, 'failure': 0})

    msg3_success_pattern = re.compile(r'.*type MSG3-RRC-C-REQ status success.*')
    msg3_failure_pattern = re.compile(r'.*MSG3-UNKNOWN status timeout.*')

    with open(file_path, 'r') as file:
        for line in file:
            if msg3_success_pattern.match(line):
                success_count += 1
                hour = get_hour_from_log(line)
                hourly_stats[hour]['success'] += 1
            elif msg3_failure_pattern.match(line):
                failure_count += 1
                hour = get_hour_from_log(line)
                hourly_stats[hour]['failure'] += 1
    print("Success Count:", success_count)
    print("Failure Count:", failure_count)
    total_attempts = success_count + failure_count
    success_rate = (success_count / total_attempts) * 100 if total_attempts > 0 else 0

    print(f"Overall Success Rate: {success_rate:.2f}%")
    print("Hourly Success Rates:")
    for hour, stats in sorted(hourly_stats.items()):
        hourly_attempts = stats['success'] + stats['failure']
        hourly_success_rate = (stats['success'] / hourly_attempts) * 100 if hourly_attempts > 0 else 0
        print(f"{hour}: {hourly_success_rate:.2f}%")

def get_hour_from_log(log_line):
    timestamp_str = log_line.split()[0] + " " + log_line.split()[1]
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    return timestamp.strftime('%Y-%m-%d %H')

if __name__ == "__main__":
    log_file_path = 'bs_log.txt'
    parse_log_file(log_file_path)
