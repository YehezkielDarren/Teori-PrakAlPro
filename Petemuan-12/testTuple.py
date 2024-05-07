kalimat = 'but soft what light in yonder window breaks'
dafkata = kalimat.split()
t = list()
for kata in dafkata:
    t.append((len(kata), kata))

t.sort(reverse=True)
print(t)

urutan = list()
for length, kata in t:
    urutan.append(kata)

print(urutan)
