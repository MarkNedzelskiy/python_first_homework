number = 0
is_six_digits_number = False

while is_six_digits_number != True:
    number = int(input("Введите шестизначное число "))
    if number > 99999 and number < 1000000:
        is_six_digits_number = True

number_first_half = 0
number_second_half = 0        
number_copy = number  #делаю копию числа чтобы переменную с числом можно было использовать дальше

for i in range(3):
    number_second_half += number_copy % 10  
    number_copy = number_copy // 10
    
for i in range(3):
    number_first_half += number_copy % 10  
    number_copy = number_copy // 10

if number_first_half == number_second_half:
    print("yes")
else:
    print("no")
