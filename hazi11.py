######################
# dobj fel egy n oldalú dobókockát 20x (n értékét kérdezze meg a program)
# készíts statisztikát, hogy melyik pööty hányszor volt
# n = 6
# 1 4 3 2 5 2 6 5 2 3 4 1 2 5 4 6 
# [1,2,3,4,5,6]  miről
# [2, 4, ...]    mennyi
import random

oldalszam = int(input("n = "))
dobasok = []
for n in range(20):
    dobasok.append(random.randint(1, oldalszam))

kivesezett = []
for szamok in dobasok:
    if szamok not in kivesezett:
        kivesezett.append(szamok)

stat = []
for szamok in kivesezett:
    db = 0
    for elem in dobasok:
        if elem == szamok:
            db += 1
    stat.append(db)

for elem in zip(kivesezett, stat):
    print("Dobott szám:",elem[0],"Ennyiszer dobtad ezt:",elem[1])
