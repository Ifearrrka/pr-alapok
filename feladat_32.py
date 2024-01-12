# feladat_032

#Listák rendezése

nyelvek = ['Python', 'C', 'C++', 'Java']
'''
    # sorbarendezi a listát
nyelvek.sort()

    # fordított sorrendbe rendezi a listát
nyelvek.reverse()  
''' 
#A listák a sort() és reverse() metódusok hatására módosulnak, elemeik rendezett sorban helyezkednek el.

keresett_elem = 'C'
if 'C' not in nyelvek:
    nyelvek.index(keresett_elem)
    print(f"Nem található a {keresett_elem}")
else:
    nyelvek.index(keresett_elem)
    print(f"Található a {keresett_elem}")
szamlalo = 0
for elem in nyelvek:
    if elem == 'Python':
        szamlalo =+ 1
        print(f"A python elem {szamlalo} ennyiszer jelent meg ")