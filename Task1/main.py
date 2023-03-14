number = 0
is_three_digits_number = False

while is_three_digits_number != True:
    number = int(input("Введите трехзначное число"))
    if number > 99 and number < 1000:
        is_three_digits_number = True

number_digits_summ = 0
number_copy = number #делаю копию числа чтобы переменную с числом можно было использовать дальше

for i in range(3):
    number_digits_summ += number_copy % 10 
    number_copy = number_copy // 10

print(number_digits_summ)