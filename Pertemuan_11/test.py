Mahasiswa_db=dict()

def isi_data(pilihan:int):
    nim=input("masukkan nim anda : ")
    if pilihan==1:
        nama=input("masukkan nama anda : ").lower()
        prodi=input("masukkan prodi anda : ").lower()
        angkatan,kode_prodi=nim[2:4],nim[:2]
        return nim,nama,prodi,angkatan,kode_prodi
    return nim

def tambahData(db,identitas):
    db[identitas[0]]={
        "Nama":identitas[1],
        "Program Studi":identitas[2],
        "Tahun Angkatan":identitas[3],
        "Kode Prodi":identitas[4]
    }
    return db

pilihan=1
for _ in range(2):
    identitasMahasiswa=list(isi_data(pilihan))
    Mahasiswa_db=tambahData(Mahasiswa_db,identitasMahasiswa)
print(Mahasiswa_db)