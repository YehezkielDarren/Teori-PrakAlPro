def odd_even(a : str):
    soal,ganjil,genap=a.split(","),[],[]
    for i in soal :
        if i.isdigit()==True:
            if int(i)%2==0:
                genap.append(i)
            else:
                ganjil.append(i)
    ganjil.sort(),genap.sort()
    jumlah=ganjil[0]+genap[0]
    ganjil.append(jumlah)
    jawab=ganjil+genap
    return " ".join(str(j) for j in jawab)

print(odd_even("1,3,5,6,2"))        