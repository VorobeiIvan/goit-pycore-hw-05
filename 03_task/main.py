import sys
from collections import defaultdict

# Функція для парсингу рядка логу
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    date_time = parts[0] + ' ' + parts[1]
    level = parts[2]
    message = parts[3].strip()
    return {'date_time': date_time, 'level': level, 'message': message}

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))

# Функція для підрахунку записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

# Функція для виведення статистики за рівнями
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<20}{'Кількість'}")
    print("-" * 30)
    for level, count in counts.items():
        print(f"{level:<20}{count}")

# Основна функція
def main():
    if len(sys.argv) < 2:
        print("Помилка: вказано недостатньо аргументів.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2].lower()
        if level not in ['info', 'debug', 'error', 'warning']:
            print("Помилка: невідомий рівень логування.")
            sys.exit(1)
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date_time']} - {log['message']}")

if __name__ == "__main__":
    main()

