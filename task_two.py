
from typing import Callable
import re


text = """Загальний дохід працівника складається з декількох \
частин: 1000.01 як основний дохід, доповнений додатковими \
надходженнями  27.45 і 324.00 доларів."""


def generator_numbers(text: str):
    """
    Функція приймає рядок та повертає генератор,
    що ітерує по всіх дійсних числах у тексті
    """

    p = r"\s\d+\.\d+\s"
    float_numbs = re.findall(p, text)
    float_numbs = "".join(float_numbs).split()
    float_numbs = list(map(float, float_numbs))
    for numb in float_numbs:
        yield numb
        
gen_numbs = generator_numbers(text)


def sum_profit(text: str, func: Callable[[str], float])-> float:
    """
    Функція обробляє дані від generator_numbers
    та підсумовує всі числа
    """

    sum_numbs = 0
    for numb in gen_numbs:
        sum_numbs += numb 
    return sum_numbs

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



