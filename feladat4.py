#Fej vagy írás
import random

user=input("Fej vagy írás?:")


pc=random.choice(["fej","írás","Fej","Írás"])

if (user == pc):
    print("Eltaláltad")
else:
    print("Nem találtad el")
