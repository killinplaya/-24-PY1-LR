money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# Переменная для отслеживания количества месяцев без долгов
months_without_debts = 0

# Цикл для расчета количества месяцев
while money_capital >= 0:
    total_income = salary  # Доход за месяц
    current_spend = spend  # Расходы за текущий месяц

    # Бюджет текущего месяца
    budget = total_income + money_capital

    # Проверяем, хватает ли бюджета для покрытия расходов
    if budget >= current_spend:
        months_without_debts += 1  # Увеличиваем счетчик месяцев
        money_capital -= max(0, current_spend - total_income)  # Уменьшаем подушку безопасности при нехватке средств
    else:
        break  # Выходим из цикла, если бюджета недостаточно

    # Увеличиваем расходы на следующий месяц
    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debts)
