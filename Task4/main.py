chocolate_m = int(input("Введите размер шоколадки m "))
chocolate_n = int(input("Введите размер шоколадки n "))

slice_cell_count = int(input("Какое количество долек вы хотите отломить от шоколадки? "))

if (slice_cell_count % chocolate_m == 0 or slice_cell_count % chocolate_n == 0) and slice_cell_count < chocolate_m * chocolate_n:
    print("yes")
else:
    print("no")