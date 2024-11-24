import json


def calculate_sum(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Используем генератор для вычисления произведений и их суммы
    total = sum(item['score'] * item['weight'] for item in data)
    return round(total, 3)


if __name__ == "__main__":
    file_path = "input.json"
    result = calculate_sum(file_path)
    print(result)
