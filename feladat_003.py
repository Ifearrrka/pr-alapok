# feladat_003
# dk9 95-oldal
print(f'Üdv néked!')
évek_száma = input('Hány éves vagy? ')
évek_száma = int(évek_száma)
if évek_száma == 0:
 print(f"Még nem születtél meg.")
elif évek_száma < 6:
    print(f"{évek_száma} éves vagy, még nem jársz általános iskolába!")
elif évek_száma >= 6 and évek_száma <= 14:
    print(f"{évek_száma} éves vagy, általános iskolába jársz!")
elif évek_száma > 14 and évek_száma <= 65:
    print(f"{évek_száma} vagy tanulsz, vagy dolgozol!")
else:
    print(f"{évek_száma} éves vagy, nyugdíjas.")
#else:
 #print(f"Egy év múlva {évek_száma+1} éves leszel.")
 #print(f"A pr nem tudta értelmezni a megadott értéket.")