"""
Morvai Marcell 
10/c
1. csoport
2023. 10. 13.
"""


jegy = int(input('Kérek egy jegyet 1-5ig : '))
if jegy == 1:
    print(f"A jegyed {jegy}, elégtelen.")
elif jegy == 2:
    print(f"A jegyed {jegy}, elégséges")
elif jegy == 3:
    print(f"A jegyed {jegy}, közepes")
elif jegy == 4:
    print(f"A jegyed {jegy}, jó")
elif jegy == 5:
    print(f"A jegyed {jegy}, jeles")
else:
    print(f'A jegyed {jegy}, ami nem megfelelő')
