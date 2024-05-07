nama_file=input("Masukkan nama file : ")
try :
    with open(nama_file) as f:
        handle=f.readlines()
except FileNotFoundError:
    print("File Not Found ", nama_file)
dictionary=dict()
for keys in handle:
    if keys.startswith("From "):
        jam=keys.split()[5].split(":")[0]
        dictionary[jam]=dictionary.get(jam,0)+1
dist_jam=list()
for hour,i in dictionary.items():
    dist_jam.append((hour,i))
dist_jam.sort()
for hour,i in dist_jam:
    print(hour,i)