def binary(number_list, target):
    awal=0
    akhir=len(number_list)-1
    while awal<=akhir:
        tengah=(awal+akhir)//2
        tebak = number_list[tengah]
        if target< tebak:
            akhir= tengah-1
        elif target> tebak:
            awal=tengah +1
        else:
            return (f"indeks ke : {tengah}")
        
        
susun = sorted([3,7,6,4,2,5,1])
print(binary(susun,4))
        