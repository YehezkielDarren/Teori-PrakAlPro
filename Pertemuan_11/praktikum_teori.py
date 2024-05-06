# eng2sp=dict() # menginisialisasikan dictionary kosong
# #1
# eng2sp["one"]="uno"
# print(eng2sp)
# #2
# eng2sp["two"]="dos"
# print(eng2sp)
# # error 
# try:
#     print(eng2sp["three"])
# except KeyError:
#     print("Value tidak ditemukan")
# # mengecek apakah terdapat data-key dalam dictionary
# print("one"in eng2sp) # cara yg benar
# print("uno"in eng2sp) # cara yang salah
# # memasukkan string ke dalam dictionary
#     # cara ke-1
# string='dutawacana'
# d=dict()
# for i in string:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
#     # cara ke-2
# string='dutawacana'
# e=dict()
# for i in string:
#     e[i]=e.get(i,0)+1
# print(e)

# a=dict()
# a["darren"]=["sayur sop","es krim","pizza"]
# a["nicho"]=["burger","pizza","pasta"]
# a["nicho"]=43
# print(a)

# a=dict()
# for i in range(3):
#     var=dict()
#     var["nama"]=input("masukkan nama anda jingg ")
#     var["no_hp"]=int(input("masukkan nomor telpon anda jingg "))
#     nim=int(input("silahkan masukkan nim luu "))
#     a[nim]=var
# print(a)