Prodi={
    "71":"Informatika",
    "72":"Sistem Informasi",
    "11":"Manajemen",
    "12":"Akuntansi",
    "61":"Arsitektur",
    "41":"Kedokteran"
}
Fakultas={
    "Fakultas Teknologi Informasi":["71","72"],
    "Fakultas Bisnis":["11","12"],
    "Fakultas Arsitektur dan Desain": ["61"],
    "Fakultas Kedokteran":["41"]
}

def isi_data(pilihan:int,daftarProdi:dict,daftarFakultas):
    nim=input("Masukkan NIM anda : ")
    if pilihan==1:
        nama=input("Masukkan nama anda : ")
        for study_code in daftarProdi.keys():
            if nim[:2]==study_code:
                prodi=daftarProdi[study_code]
                break
        for faculty,stdy_code in daftarFakultas.items():
            if nim[:2] in stdy_code:
                fakultas=faculty
                break
        angkatan,kode_prodi="20"+nim[2:4],nim[:2]
        return nim,nama,prodi,angkatan,fakultas
    return nim

def tambahData(db,identitas):
    db[identitas[0]]={
        "Nama":identitas[1],
        "NIM":identitas[0],
        "Program Studi":identitas[2],
        "Tahun Angkatan":identitas[3],
        "Fakultas":identitas[4]
    }
    return db

def lihatData(db:dict):
    print("==============")
    print("DATA MAHASISWA")
    print("==============")
    for stdnt_num in db.keys():
        for keys,vals in db[stdnt_num].items():
            print(f"{keys}:{vals}")
        print()
    print("===Data Selesai===")

def hapusData(db:dict,nim):
    for stdnt_num in db.keys():
        if nim==stdnt_num:
            db[stdnt_num].clear()
            return db
    else:
        return db
def main():
    Mahasiswa_db=dict()
    yes_no=["Y","N"]
    while True:
        print("=======================")
        print("Database Mahasiswa UKDW")
        print("=======================")
        print("Pilihan : ")
        print("1. Menambah Data")
        print("2. Melihat Data")
        print("3. Menghapus Data")
        try:
            pilihan=int(input("\nPilih no 1 - 3 : "))
        except ValueError:
            print("\nPilihan berupa angka\n")
        else:
            print()
            if pilihan<1 or pilihan>3:
                print("\nPilihan hanya 1-3\n")
                continue
            elif pilihan==1:
                while True:
                    identitasMahasiswa=list(isi_data(pilihan,Prodi,Fakultas)) # nama,nim,prodi,angkatan,kode_prodi
                    Mahasiswa_db=tambahData(Mahasiswa_db,identitasMahasiswa)
                    print("====Data Berhasil Di Update====")
                    lanjut=input("Apakah ingin lanjut ? (Y/N) ").upper()
                    if lanjut==yes_no[0]:
                        print()
                        continue
                    else:
                        print()
                        break
            elif pilihan==2:
                lihatData(Mahasiswa_db)
            else:
                identitasMahasiswa=isi_data(pilihan,Prodi,Fakultas)
                Mahasiswa_db=hapusData(Mahasiswa_db,identitasMahasiswa)
                print("====Data Berhasil Terhapus====")

main()