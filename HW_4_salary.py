def total_salary(path):
    sum_salary = 0 # загальна сума
    count = 0 # лічильник записів

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                name, salary = line.strip().split(',') # розділення рядка на ім'я та зарплату
                sum_salary += float(salary)
                count += 1
            except ValueError:   # вийняток для некоректних данних
                print(f"Некоректно введені дані: {line.strip()}")

    average_salary = float(sum_salary / count if count > 0 else 0) # розрахунок середньої зарплати

    return sum_salary, average_salary

path = 'salaries.txt' # вказуємо шлях до файлу із зарплатами
result = total_salary(path)

# result[0] загальна сума зарплат, result[1] середня сума зарплат
print(f"Сума зарплат: {result[0]}, Середня зарплата: {result[1]}")