import numpy as np

# tworzenie pola o zadanych wymiarach
X = input("Proszę podaj rozmiar X pola: ")
X = int(X)
Y = input("oraz Y: ")
Y = int(Y)
L = input("A teraz podaj ilość ludzi: ")
L = int(L)
print("\n")
l=0
pole = [[0 for x in range(X)] for y in range(Y)] # tworzenie pola o rozmiarach [X;Y] narazie wypełnionego zerami (pustymi miejscami)
# losowe wypełnianie pola zadaną liczbą ludzi
# # pole = np.random.randint(0, 1, size=(Y, X))
# while(l < L): # wypełnianie pola wskazaną ilością ludzi
#     print("while " + str(l)) # wyświetla informację ile razy została wykonana pętla (fyi)
#     for x in range(X): #
#         for y in range(Y): # przemiatamy wszystkie miejsca pola
#             if(l<L): # jeśli w polu nadal jest mniejsza ilość ludzi, niż wskazana, to wykonujemy poniższą instrukcję
#                 if(pole[x][y]!=1): # jeżeli w obecnie rozpatrywanym miejscu pola nie ma człowieka (cyfra 1, w przeciwieństwie do 0, które reprezentuje puste miejsce), to wykonujemy poniższa instrukcję
#                     pole[x][y]=np.random.randint(0,2) # losujemy dla danego miejsca pola 0 albo 1, żeby rozmieścić ludzi losowo, a nie musieć tego robić ręcznie
#                     if(pole[x][y]==1):
#                         l+=1 # jeśli w rozpatrywanym obecnie miejscu pola został wylosowany i wstawiony człowiek (cyfra 1), to licznik się zwiększa i przechodzimy do kolejnego miejsca w polu; cały proces się powtarza, aż pole nie zostanie wypełnione wskazaną ilością ludzi
#                         print(l)
while(l < L): # wypełnianie pola wskazaną ilością ludzi
    x = np.random.randint(0,X) # losujemy miejsce (X)
    y = np.random.randint(0,Y) # losujemy miejsce (Y)
    if(l<L): # jeśli w polu nadal jest mniejsza ilość ludzi, niż wskazana, to wykonujemy poniższą instrukcję
        if(pole[y][x]!=1): # jeżeli w obecnie rozpatrywanym miejscu pola nie ma człowieka (cyfra 1, w przeciwieństwie do 0, które reprezentuje puste miejsce), to wykonujemy poniższa instrukcję
            pole[y][x] = np.random.randint(0,2) # losujemy dla danego miejsca pola 0 albo 1, żeby rozmieścić ludzi losowo, a nie musieć tego robić ręcznie
            if(pole[y][x]==1):
                l+=1 # jeśli w rozpatrywanym obecnie miejscu pola został wylosowany i wstawiony człowiek (cyfra 1), to licznik się zwiększa i przechodzimy do kolejnego miejsca w polu; cały proces się powtarza, aż pole nie zostanie wypełnione wskazaną ilością ludzi
print(np.matrix(pole))
print("\n")


# tworzenie tabeli ludzi (miejsca pola, w których są ludzie)
tabela_wspolrzednych_ludzi = [[0 for i in range(3)] for l in range(L)]
l=0
for y in range(Y):
    for x in range(X):
        if(pole[y][x]==1):
            tabela_wspolrzednych_ludzi[l]=[l+1,x+1,y+1]
            l+=1
print(np.matrix(tabela_wspolrzednych_ludzi))
print("\n")


# wybór i przypisanie osób
tabela_wyboru = [[0 for i in range(2)] for l in range(L)]
for l in range(L):
    tabela_wyboru[l]=[l+1,np.random.randint(0,L)+1]
print(np.matrix(tabela_wyboru))
print("\n")


# tabela przedstawiająca końcowe współrzędne posczególnych osób, w miejscu najbliżej celu
tabela_drogi = [[0 for i in range(3)] for l in range(L)] # [nr osoby, nr osoby przez nia wybranej][wspolrzedne x i y osoby][wspolrzedne x i y już przy osobie przez nią wybranej]
tabela_wektorow = [[0 for i in range(3)] for l in range(L)]
for l in range(L):
    tabela_drogi[l][0] = l+1
    tabela_wektorow[l][0] = l+1
    tabela_wektorow[l][1] = [tabela_wspolrzednych_ludzi[tabela_wyboru[l][1]-1][1] - 1 - tabela_wspolrzednych_ludzi[l][1]] # przesunięcie w osi X
    tabela_wektorow[l][2] = [tabela_wspolrzednych_ludzi[tabela_wyboru[l][1]-1][2] - 1 - tabela_wspolrzednych_ludzi[l][2]] # przesunięcie w osi Y
    tabela_drogi[l][1] = tabela_wspolrzednych_ludzi[l][1] + tabela_wektorow[l][1]
    tabela_drogi[l][2] = tabela_wspolrzednych_ludzi[l][2] + tabela_wektorow[l][2]
print(tabela_drogi)
print("\n")

