import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    # Читаем данные из CSV-файла
    with open(INPUT_FILENAME, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        data = [row for row in reader]  # Список словарей для каждой строки CSV

    # Записываем данные в JSON-файл
    with open(OUTPUT_FILENAME, mode='w') as json_file:
        json.dump(data, json_file, indent=4)  # Запись с отступами для форматирования


if __name__ == '__main__':
    # Вызов функции
    task()

    # Чтение и вывод JSON-файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")