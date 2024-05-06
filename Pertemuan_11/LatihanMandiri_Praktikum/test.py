def domainAkun(txt:str):
    try:
        text=open(txt)
    except FileExistsError:
        print("File Not Found!!!")
    else:
        domain_=dict()
        for words in text:
            if words.startswith("From: "):
                akun=words.split()[1].split("@")
                domain=akun[-1]
                domain_[domain]=domain_.get(domain,0)+1
        return domain_

nama_file=input("Masukkan Nama File : ")
print(domainAkun(nama_file))