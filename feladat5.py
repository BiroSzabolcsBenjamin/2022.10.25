import random


N=int(input("Hány elemmel akarsz dolgozni: "))

Lszamok=[]

for i in range (N): 
    Lszamok.append(random.randint(-100,100))

print(Lszamok)

#a rész
negativdb=0
for szam in Lszamok:
    if(szam<0):
        negativdb+=1

print("Negativ számok száma: ", negativdb)

#b rész
print(max(Lszamok)-min(Lszamok))

#c csökkenő
Lszamok.sort()
Lszamok.reverse()
print(Lszamok)