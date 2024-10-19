disk_capacity = 1.44 #mb
pages = 100
lines = 50
chars = 25
bytes = 4

disk_capacity_bytes = disk_capacity * 1024 * 1024

book_size_bytes = pages * lines * chars * bytes

number_of_books = disk_capacity_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(number_of_books))
