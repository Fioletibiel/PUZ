import numpy as np

# tworzenie pola o zadanych wymiarach
X = input("Proszę podaj rozmiar X pola: ")
X = int(X)
Y = input("oraz Y: ")
Y = int(Y)
L = input("A teraz podaj ilość ludzi: ")
L = int(L)
print("\n")

# wybór i przypisanie osób
tabela_wyboru = [[0 for i in range(2)] for l in range(L)]
for l in range(L):
    tabela_wyboru[l]=[l+1,np.random.randint(0,L)+1]
print(np.matrix(tabela_wyboru))
print("\n")


# losowe wypełnianie pola zadaną liczbą ludzi
pole = [[0 for x in range(X)] for y in range(Y)]
l=0
while(l < L):
    x = np.random.randint(0,X)
    y = np.random.randint(0,Y)
    if(l<L):
        if(pole[y][x]!=1):
            pole[y][x] = np.random.randint(0,2)
            if(pole[y][x]==1):
                l+=1
print(np.matrix(pole))
print("\n")

# stworzenie początkowej tabeli rozmieszczenia ludzi (miejsca pola, w których są ludzie)
tabela_wspolrzednych_ludzi = [[0 for i in range(3)] for l in range(L)]
l=0
for y in range(Y):
    for x in range(X):
        if(pole[y][x]==1):
            tabela_wspolrzednych_ludzi[l]=[l+1,x+1,y+1]
            l+=1

# symulacja ruchu ludzi
tabela_wspolrzednych_ludzi = [[0 for i in range(3)] for l in range(L)]
tabela_celu = [[0 for i in range(3)] for l in range(L)]
tabela_wektorow = [[0 for i in range(3)] for l in range(L)]
tabela_ruchu = [[0 for i in range(3)] for l in range(L)]
tabela_ruchu = float(tabela_ruchu)
while(tabela_wspolrzednych_ludzi!=tabela_celu):
    for l in range(L):
        tabela_celu[l][0], tabela_wektorow[l][0], tabela_ruchu[l][0] = l+1
        tabela_wektorow[l][1] = [tabela_wspolrzednych_ludzi[tabela_wyboru[l][1]-1][1] - 1 - (tabela_wspolrzednych_ludzi[l][1] - 1)] # przesunięcie w osi X
        tabela_wektorow[l][2] = [tabela_wspolrzednych_ludzi[tabela_wyboru[l][1]-1][2] - 1 - (tabela_wspolrzednych_ludzi[l][2] - 1)] # przesunięcie w osi Y
        tabela_celu[l][1] = tabela_wspolrzednych_ludzi[l][1] + tabela_wektorow[l][1]
        tabela_celu[l][2] = tabela_wspolrzednych_ludzi[l][2] + tabela_wektorow[l][2]
        ilosc_okresow = np.min(abs(tabela_wektorow))
        tabela_ruchu[l][1] = tabela_wspolrzednych_ludzi[l][1] + tabela_wektorow[l][1]/ilosc_okresow
        tabela_ruchu[l][2] = tabela_wspolrzednych_ludzi[l][2] + tabela_wektorow[l][2]/ilosc_okresow
        tabela_ruchu=int(tabela_ruchu)
        tabela_wspolrzednych_ludzi[l][1] = tabela_ruchu[l][1]
        tabela_wspolrzednych_ludzi[l][2] = tabela_ruchu[l][2]

# odtworzenie tabeli rozmieszczenia ludzi / stworzenie końcowej tabeli rozmieszczenia ludzi