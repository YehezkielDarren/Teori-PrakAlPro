data=('Yehezkiel Darren Putra Wardoyo', '71231023', 'Sleman, DI.Yogyakarta')
nim=data[1]
nama=data[0]
alamat=data[2]
print("NIM\t\t: ",nim)
print("NAMA\t\t: ",nama)
print("ALAMAT\t\t: ",alamat)
print()
nama=nama.split()
print("NIM\t\t: ", tuple(nim))
print("Nama Depan\t: ", tuple(nama[0]))
print("NIM\t\t: ", tuple(nama[-1::-1]))

