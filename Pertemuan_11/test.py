#data list
nama=["darren","ndus","calvin"]
umur=[19,20,20]
user=dict()
for i in range(min(len(nama),len(umur))):
    user[nama[i]]=umur[i]
print(user)