def dictMerger(*dictionaries):
    dictMergered = {}
    for d in dictionaries:
        for key, value in d.items():
            if key not in dictMergered:
                if type(value) != list:
                    dictMergered[key] = value
                else:
                    dictMergered[key] = [value]

            else:
                if type(dictMergered[key]) != list:
                    dictMergered[key] = [dictMergered[key]]
                if type(value) == list:
                    dictMergered[key].append(value)
                else:
                    dictMergered[key].append(value)
    return dictMergered

# Test Case

a = {"nama" : "Maria", "tempat" : "Jakarta"}
b = {"nama" : ["Harris", "Kurniadi"], "tempat" : "Yogyakarta"}
c = {"nama" : "Santoso", "tempat" : "Solo", "kuliah":"UKDW"}

print(dictMerger(a,b,c))

d = {"kelas" : "Alpro"}
e = {"NIM" : "71190434"}
f = {"ipk" : 4.1}
g = {"prodi" : "Informatika"}
h = {"status" : True}

print(dictMerger(d,e,f,g,h))