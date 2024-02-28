def binary_search(number_list,target):
    number_list.sort()
    mulai=0
    akhir=len(number_list)-1
    while mulai <= akhir:
        tengah= (mulai+akhir)//2
        if number_list[tengah]<number_list[target]:
            akhir = tengah+1
        elif number_list[tengah]>number_list[target]:
            akhir = tengah -1
        else:
            return tengah 
    return None 


angka_acak= [11,23,91,51,10,1]
target= 1
print(binary_search(angka_acak, target))




    