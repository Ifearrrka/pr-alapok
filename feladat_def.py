# feladat_015
"""
Kérjük be a vezeték és keresztnevünket
"""
vez = input("Kérek egy vezetéknevet")
ker = input("Kérek egy keresztnevet")
def nevf(vnev, knev):
    nevem = vnev + ' ' + knev
    return nevem

print(f"A nevem: {nevf(vez,ker)}")