def deret(a,b,c):
    for i in range(0, c-1, b):
        print(a)
    return a

U1=int(input("masukkan bilangan awal : "))
b=int(input("Masukkan selisih : "))
Un = int(input("masukkan banyak suku :"))

print(deret(U1,b,Un))