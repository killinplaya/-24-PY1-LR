salary = 5000 # Ежемесячная зарплата
spend = 6000 # Траты за первый месяц
months = 10 # Количество месяцев без долгов
increase = 0.03 # Ежемесячный рост цен

# Общие сбережения
total_savings = 0

for month in range(months):
    # Доход за месяц
    total_income = salary

    # Расходы за текущий месяц
    current_spend = spend

    # Покрытие расходов зарплатой
    total_income -= current_spend

    # Если нехватка средств, добавляем к сбережениям
    if total_income < 0:
        total_savings += abs(total_income)

        # Увеличиваем расходы
    spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total_savings))
