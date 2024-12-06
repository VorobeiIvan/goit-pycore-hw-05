from src.commands import *
import sys

def main ():
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)


if __name__ == "__main__":
    main()