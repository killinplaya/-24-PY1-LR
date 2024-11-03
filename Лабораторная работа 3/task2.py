def find_common_participants(group1, group2, delimiter=","):
    # Разделяем строки по заданному разделителю
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим пересечение и сортируем результат
    common_participants = sorted(participants1 & participants2)
    return common_participants


# Пример использования функции с разделителем, отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызываем функцию с разделителем '|'
common = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники:", common)
