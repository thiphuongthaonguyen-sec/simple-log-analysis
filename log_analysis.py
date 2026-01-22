from collections import Counter
import re

LOG_FILE = "logs/auth.log"

failed_pattern = re.compile(r"Failed password.*from ([0-9.]+)")

def analyze_log(file_path):
    failed_ips = []

    with open(file_path, "r") as f:
        for line in f:
            match = failed_pattern.search(line)
            if match:
                failed_ips.append(match.group(1))

    counts = Counter(failed_ips)
    return counts


if __name__ == "__main__":
    results = analyze_log(LOG_FILE)

    print("Failed login attempts by IP:")
    for ip, count in results.items():
        print(f"{ip}: {count} attempts")

    print("\nPotential brute-force sources:")
    for ip, count in results.items():
        if count >= 3:
            print(f"- {ip}")
