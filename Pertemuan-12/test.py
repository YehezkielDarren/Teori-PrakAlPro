alphabetical=" abcdefghijklmnopqrstuvwxyz"
test="watch your step"
words=test.split()
hasil=""
for word in words:
    for i in word:
        angka=(14*alphabetical.index(i)+21)%26
        print(angka)
        hasil+=alphabetical[angka]
print(hasil)
        