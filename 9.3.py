import sys
import numpy as np


def getch():
    getchar = input("")
    getchar = None

# tworzenie_pola
X = input("Proszę podaj rozmiar X pola: ")
X = int (X)
Y = input("oraz Y: ")
Y = int(Y)
L = input("A teraz podaj ilość ludzi: ")
L = int (Y)
print("\n")
l=0
pole = [[0 for x in range(X)] for y in range(Y)] # tworzenie pola o rozmiarach [X;Y] narazie wypełnionego zerami (pustymi miejscami)
# pole = np.random.randint(0, 1, size=(Y, X))
while(l < L): # wypełnianie pola wskazaną ilością ludzi
    print("while " + str(l)) # wyświetla informację ile razy została wykonana pętla (fyi)
    for x in range(X): #
        for y in range(Y): # przemiatamy wszystkie miejsca pola
            if(l<L): # jeśli w polu nadal jest mniejsza ilość ludzi, niż wskazana to wykonujemy poniższą instrukcję
                if(pole[x][y]!=1): # jeżeli w obecnie rozpatrywanym miejscu pola nie ma człowieka (cyfra 1, w przeciwieństwie do 0, które reprezentuje puste miejsce), to wykonujemy poniższa instrukcję
                    pole[x][y]=np.random.randint(0,2) # losujemy dla danego miejsca pola 0 albo 1, żeby rozmieścić ludzi losowo, a nie musieć tego robić ręcznie
                    if(pole[x][y]==1):
                        l+=1 # jeśli w rozpatrywanym obecnie miejscu pola został wylosowany i wstawiony człowiek (cyfra 1), to licznik się zwiększa i przechodzimy do kolejnego miejsca w polu; cały proces się powtarza, aż pole nie zostanie wypełnione wskazaną ilością ludzi
                        print(l)
print(np.matrix(pole))




# tabela_ludzi=[]
# for x in range(X):
#     for y in range(Y):
#         if(pole[x][y]==1):
#             tabela_ludzi.append(x,y)

#print(tabela_ludzi)

# a = []
# for x in range(8):
#     row = []
#     for y in range(8):
#         row.append(0)
#     a.append(row)

getch()
sys.exit(0)