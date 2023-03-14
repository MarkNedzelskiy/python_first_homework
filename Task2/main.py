origami_summ = int(input("Введите общее количество сделанных журавликов "))

kate_count = 0
sergei_count = 0
petia_count = 0

is_counting = True
counting_var = 1

while is_counting == True:
    if counting_var  * 6 == origami_summ:
        kate_count = counting_var * 4
        sergei_count = counting_var
        petia_count = counting_var
        is_counting = False
    else:
        counting_var += 1
        
print(sergei_count)
print(kate_count)
print(petia_count)