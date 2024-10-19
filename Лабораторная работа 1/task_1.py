numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total_sum = sum(num for num in numbers if num is not None)

count_with_none = len(numbers)

average = total_sum / (count_with_none)

modified_list = [average if num is None else num for num in numbers]

print("Измененный список:", modified_list)

