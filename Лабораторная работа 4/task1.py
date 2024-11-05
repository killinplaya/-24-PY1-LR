import json  # Импортируем модуль для работы с JSON

def task() -> float:

    # Открываем JSON файл и загружаем данные
    with open('input.json', 'r') as file:
        data = json.load(file)  # data будет списком словарей

    # Переменная для накопления суммы произведений
    total_sum = 0.0

    # Проходим по каждому словарю в списке
    for item in data:
        # Извлекаем значения "score" и "weight" и вычисляем произведение
        product = item["score"] * item["weight"]
        # Добавляем произведение к общей сумме
        total_sum += product

    # Возвращаем сумму произведений, округленную до 3 знаков
    return round(total_sum, 3)

# Вызываем функцию и выводим результат
print(task())