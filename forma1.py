"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Melyik versenyző nyerte a legkevesebb futamot?
4. Ki teljesítette a legtöbb futamot?
5. Átlagosan hány futamot teljesítettek a versenyzők?"

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerezte a legtöbb futamgyőzelmet?

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""
import statistics as st

versenyzok = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        csapat = adatok[1]
        gyozelem = int(adatok[2])
        futam = int(adatok[3])
        versenyzo = {'nev': nev, 'csapat': csapat, 'gyozelem': gyozelem, 'futam': futam}
        versenyzok.append(versenyzo)

print(f'{versenyzok=}')

#1. feladat
versenyzok_szama = 0
for i in versenyzok:
    if i["nev"] != "":
        versenyzok_szama += 1

#2. feladat
gyozelmek_listaja = []
legtobb_gyozelem = versenyzok[0]
for i in versenyzok:
    gyozelmek_listaja.append(i["gyozelem"])
legtobb_gyozelem = versenyzok[gyozelmek_listaja.index(max(gyozelmek_listaja))]

#3. feladat
legkevesebb_gyozelem = versenyzok[gyozelmek_listaja.index(min(gyozelmek_listaja))]

#4. feladat
futamok_listaja = []
legtobb_futam = versenyzok[0]
for i in versenyzok:
    futamok_listaja.append(i["futam"])
legtobb_futam = versenyzok[futamok_listaja.index(max(futamok_listaja))]

#6. feladat


print(f"1. A beolvasott fájlban összesen {versenyzok_szama} versenyző szerepel.")
print(f"2. A legtöbb futamot nyert versenyző: {legtobb_gyozelem["nev"]}")
print(f"3. A legkevesebb futamot nyert versenyző: {legkevesebb_gyozelem["nev"]}")
print(f"4. A legtöbb futamot teljesített versenyző: {legtobb_futam["nev"]}")
print(f"5. Az átlagos futamszám: {round(st.mean(i["futam"] for i in versenyzok), 2)}")
print(f"***A legtöbb futamgyőzelmet szerző csapat: ____")