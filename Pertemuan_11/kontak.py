def cari_berdasar_operator(kontak:dict,operator:dict,namaKartu:str):
    hasil=[]
    for names,contacts in kontak.items():
        if contacts[:4] in operator[namaKartu]:
            hasil.append(names)
    return hasil


contact,operator={
    'Badu' : '089879938817',
    'Hana' : '0818662514110',
    'Seto' : '08122290909',
    'Adi' : '0856808080012',
    'Pace' : '0858000000000'
},{
    "telkomsel":["0812","0822"],
    "im3":["0856","0857","0858"],
    "three":"0898",
    "xl":["0817","0818"]
}
cariKontak=input("masukkan nama operator : ").lower()
print(cari_berdasar_operator(contact,operator,cariKontak))
