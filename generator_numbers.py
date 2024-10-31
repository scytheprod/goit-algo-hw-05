import re


text = "Загальний дохід працівника складається з декількох частин: 1000.13 або 1001.12 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    salary = re.findall(r'\b\d+\.\d+\b', text)
    float_numbers = [float(num) for num in salary]
    for number in float_numbers:
        yield number

def sum_profit(any_text, any_func):
    any_func = generator_numbers(any_text)
    summary = sum(any_func)
    return summary

total_income = sum_profit(text, generator_numbers)
print(f"Загальна зарплатня складає: {total_income:.2f}")















