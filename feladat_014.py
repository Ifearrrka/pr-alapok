# feladat_012
# be: pozitív egész 
# ki: a szám páros vagy páratlan
#def használata
#   utasitás

def beker_egy_szamot():
szam3 = int(input("Kérek egy egész számot : "))


def megoldas_if_else():
    if szam3 % 2 == 0:
        print(f"A számod {szam3} páros!")
    else:
        print(f"A számod {szam3} páratlan!")
        
def megoldas_if_elif():
    if szam3 % 2 == 0:
        print(f"A számod {szam3} páros!")
    elif szam3 % 2 == 1:
        print(f"A számod {szam3} páratlan! ")
        
#itt kezdődik a futtatással
beker_egy_szamot()
megoldas_if_else()
megoldas_if_elif()
"""
if szam % 2 == 0:
    print(f"A számod {szam} páros!")
else:
    print(f"A számod {szam} páratlan!")
"""
"""
if szam % 2 == 0:
    print(f"A számod {szam} páros!")
elif szam % 2 == 1:
    print(f"A számod {szam} páratlan!")
"""
"""
if szam % 2 == 0:
    print(f"A számod {szam} páros!")
elif szam % 2 != 0:
    print(f"A számod {szam} páratlan!")
"""
if szam % 2 == 0:
    print(f"A számod {szam} páros!")
if szam % 2 == 1:
    print(f"A számod {szam} páratlan!")