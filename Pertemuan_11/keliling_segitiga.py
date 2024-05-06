def kelilingSegitga(dictionary:dict):
    namaSegitiga="".join(dictionary.keys())
    hasil,points=0,list(dictionary.values())
    for i in range(len(points)):
        hasil+=(((points[(i+1)%3][0])-(points[i][0]))**2+((points[(i+1)%3][1])-(points[i][1]))**2)**0.5
    return f"{namaSegitiga} memiliki keliling {hasil:.4f}"
    
segitiga={
    "A": [1, 1],
    "B": [5, 1],
    "C": [3, 7]
}
print(kelilingSegitga(segitiga)) 