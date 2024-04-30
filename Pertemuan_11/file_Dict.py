# try:
#     with open("romeo.txt") as f:
#         text=f.readlines()
#     d=dict()
#     for line in text:
#         line=line.strip("\n").split()        
#         for word in line:
#             if word not in d:
#                 d[word]=1
#             else:
#                 d[word]+=1
# except:
#     print("File not found!!")
#     exit()
# print(d)

# try:
#     with open("romeo.txt") as f:
#         text=f.readlines()
#     d=dict()
#     for line in text:
#         line=line.strip("\n").split()        
#         for word in line:
#             d[word]=d.get(word,0)+1
# except:
#     print("File not found!!")
#     exit()
# print(d)