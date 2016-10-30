seznam=['Tim','Lev','Amon','Žiga','Tilen','Tim','Luka','Martin','Nal']

print('a primer:\n')
for i in seznam:
    print(i)

print('\nb primer:\n')
for i in seznam:
    print(i)
    for j in seznam:
        print(j)

print('\nc primer:\n')
for i in range(0,len(seznam)):
    print(seznam[i])
