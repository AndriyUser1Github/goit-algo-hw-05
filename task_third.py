import sys
import re
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    """
    Функція приймає рядки лог-файлу,
    розбиває по пробілу на підрядки,
    створює словник, значенями якого 
    виступають підрядки з рядка лог-файлу     
    """ 

    if not re.match(r"\d{4}\-\d{2}\-\d{2}", date):
        return None
    if not re.match(r"\d{2}\:\d{2}\:\d{2}", time):
        return None
        
    date, time, level, *message = line.split(" ")
    return {"date": date, "time": time, "leve": level, "massage": " ".join(message)}


def load_logs(file_path: str) -> list:
    """
    Функція приймає рядок-адресу лог-файлу,
    викликає parse_log_line для обробки рядків
    лог-файлу, створює список з рядків
    """

    with open(file_path, "r", encoding="UTF-8") as logfile:
        log_lines = list(filter(lambda x: x is not None, (map(parse_log_line, logfile.readlines()))))
    return log_lines


def filter_logs_be_level(logs: list, level: str) -> dict:
    """
    Функція фільтрує логи за рівнем логування та
    виводить результат в термінал
    """

    return list(filter(lambda x: x['level'] == level, logs))


def count_logs_be_level(logs: list) -> dict:
    """
    Функція підраховує та повертає кількість 
    записів для кожного рівня логування  
    """
    counter = defaultdict()
    counter.default_factory = int
    for log in logs:
        counter[log["level"]] += 1
    return dict(counter)


def display_log_counts(counts: dict):
    """
    Функція форматує та виводить 
    результати на дисплей
    """

    print(f"{'Рівень логування': 20}| Кількість")
    print(f"{'-'*20}|{'-'*10}")
    print("\n".join(list(map(lambda x: f"{x: 20}| {counts[x]}", counts))))


if __name__ == "__main__":
    file_name = sys.argv[1]
    logs = load_logs(file_path=file_name)
    display_log_counts(count_logs_be_level(logs))


if len(sys.argv) == 3:
    level = sys.argv[2]
    logs = filter_logs_be_level(logs, level)
    print()
    print(f"Деталі логів для рівня '{level}': ")
    print(''.join(map(lambda x: f"{x['date']} {x['time']} - {x['message']}", logs)))

