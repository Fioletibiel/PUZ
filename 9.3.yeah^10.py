import numpy as np
import subprocess
import os
def odswiez_ekran():
    subprocess.call("cls", shell=True)
def poczekaj(czas):
    cz=0
    while(cz<czas):
        os.system('cls')
        cz+=1

# tworzenie pola o zadanych wymiarach
X = input("Proszę podaj rozmiar X pola: ")
X = int(X)
while(X<2):
    X = input("Rozmiar X pola musi być większy od 1: ")
    X = int(X)
Y = input("oraz Y: ")
Y = int(Y)
while(Y<2):
    Y = input("Rozmiar Y pola musi być większy od 1: ")
    Y = int(Y)
L = input("A teraz podaj ilość ludzi: ")
L = int(L)
while(L<2):
    L = input("Ilość ludzi musi być większa od 1: ")
    L = int(L)
print("\n")

# # wybór i przypisanie osób
# tabela_wyboru = [[0 for i in range(2)] for l in range(L)]
# for l in range(L):
#     tabela_wyboru[l] = [l+1,np.random.randint(0,L)+1]
#     while(tabela_wyboru[l][1]==tabela_wyboru[l][0]):
#         tabela_wyboru[l] = [l+1, np.random.randint(0,L)+1]

# # wybór i przypisanie osób
# tabela_wyboru = [[0 for i in range(2)] for l in range(L)]
# bul='prawda'
# for l in range(L):
#     tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
#     for m in range(l-1):
#         if(tabela_wyboru[l][1]==tabela_wyboru[m][1]):
#             bul = 'falsz'
#     while(tabela_wyboru[l][1]==tabela_wyboru[l][0] or bul=='falsz'):
#         tabela_wyboru[l] = [l+1, np.random.randint(0,L)+1]
#         bul='prawda'
#         for m in range(l-1):
#             if (tabela_wyboru[l][1] == tabela_wyboru[m][1]):
#                 bul = 'falsz'

# # wybór i przypisanie osób
# tabela_wyboru = [[0 for i in range(2)] for l in range(L)]
# bul='prawda'
# for l in range(L):
#     print(l+1)
#     tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
#     print(tabela_wyboru[l])
#     for m in range(abs(l-1)):
#         if(tabela_wyboru[l][1]==tabela_wyboru[m][1]):
#             bul = 'falsz'
#     while (tabela_wyboru[l][1] == tabela_wyboru[l][0]):
#         tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
#     if(l>0):
#         while(tabela_wyboru[l][1]==tabela_wyboru[l][0] or bul=='falsz'):
#             tabela_wyboru[l] = [l+1, np.random.randint(0,L)+1]
#             print(tabela_wyboru[l])
#             bul='prawda'
#             for m in range(abs(l-1)):
#                 if (tabela_wyboru[l][1] == tabela_wyboru[m][1]):
#                     bul = 'falsz'


# wybór i przypisanie osób
tabela_wyboru = [[0 for i in range(2)] for l in range(L)]
bul='falsz'
while(bul=='falsz'):
    bul='prawda'
    for l in range(L):
        if(l==0):
            tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
            while (tabela_wyboru[l][1] == tabela_wyboru[l][0]):
                tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
        if(l==1):
            tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
            while (tabela_wyboru[l][1] == tabela_wyboru[l][0]):
                tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
            if(tabela_wyboru[l][1]==tabela_wyboru[0][1]):
                bul = 'falsz'
            while(tabela_wyboru[l][1]==tabela_wyboru[l][0] or bul=='falsz'):
                tabela_wyboru[l] = [l+1, np.random.randint(0,L)+1]
                bul='prawda'
                if (tabela_wyboru[l][1] == tabela_wyboru[0][1]):
                    bul = 'falsz'
        if(1<l<L-1):
            tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
            while (tabela_wyboru[l][1] == tabela_wyboru[l][0]):
                tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
            for m in range(l):
                if(tabela_wyboru[l][1]==tabela_wyboru[m][1]):
                    bul = 'falsz'
            while(tabela_wyboru[l][1]==tabela_wyboru[l][0] or bul=='falsz'):
                tabela_wyboru[l] = [l+1, np.random.randint(0,L)+1]
                bul='prawda'
                for m in range(l):
                    if (tabela_wyboru[l][1] == tabela_wyboru[m][1]):
                        bul = 'falsz'
        if(l==L-1):
            tabela_wyboru[l] = [l + 1, np.random.randint(0, L) + 1]
            for m in range(l):
                if(tabela_wyboru[l][1]==tabela_wyboru[m][1]):
                    bul = 'falsz'
            while(bul=='falsz'):
                tabela_wyboru[l] = [l+1, np.random.randint(0,L)+1]
                bul='prawda'
                for m in range(l):
                    if (tabela_wyboru[l][1] == tabela_wyboru[m][1]):
                        bul = 'falsz'
            if(tabela_wyboru[l][1]==tabela_wyboru[l][0]):
                bul='falsz'



print("Tabela wyboru:")
print(np.matrix(tabela_wyboru))
print("\n")

# losowe wypełnianie pola zadaną liczbą ludzi
pole = [['' for x in range(X)] for y in range(Y)]
l=0
while(l < L):
    x = np.random.randint(0,X)
    y = np.random.randint(0,Y)
    if(pole[y][x]!='©'):
        pole[y][x] = str(np.random.randint(0,2))
        if(pole[y][x]=='0'):
            pole[y][x]=''
        else:
            pole[y][x]='©'
            l+=1
print("Pole przed przetasowaniem:")
print(np.matrix(pole))
print("\n")

# stworzenie początkowej tabeli rozmieszczenia ludzi (miejsca pola, w których są ludzie)
tabela_wspolrzednych_ludzi = [[0 for i in range(3)] for l in range(L)]
l=0
for y in range(Y):
    for x in range(X):
        if(pole[y][x]=='©'):
            tabela_wspolrzednych_ludzi[l]=[l+1,x+1,y+1]
            l+=1
print("Tabela współrzędnych ludzi przed przetasowaniem:")
print(np.matrix(tabela_wspolrzednych_ludzi))
print("\n")

# def losowanie():
#     los = np.random.randint(0, 2)
#     if(los==0):
#         los=-1
#     return los

# symulacja ruchu ludzi
tabela_wektorow = [[0 for i in range(2)] for l in range(L)]
k=0
wszyscy_na_miejscu = ['falsz' for l in range(L)]
wszyscy_na_miejscu_lol='falsz'
while(wszyscy_na_miejscu_lol!='prawda'):

    for i in range(L):
        tabela_wektorow[i][0] = tabela_wspolrzednych_ludzi[tabela_wyboru[i][1] - 1][1] - 1 - (tabela_wspolrzednych_ludzi[i][1] - 1) # przesunięcie w osi X - 1
        tabela_wektorow[i][1] = tabela_wspolrzednych_ludzi[tabela_wyboru[i][1] - 1][2] - 1 - (tabela_wspolrzednych_ludzi[i][2] - 1) # przesunięcie w osi Y - 1

        if(tabela_wspolrzednych_ludzi[tabela_wyboru[i][1] - 1][1]-2 < tabela_wspolrzednych_ludzi[i][1] < tabela_wspolrzednych_ludzi[tabela_wyboru[i][1] - 1][1]+2):
            wszyscy_na_miejscu[i]='prawda'
            for otaa in range(L):
                if(otaa!=i):
                    if(tabela_wspolrzednych_ludzi[i][1] == tabela_wspolrzednych_ludzi[otaa][1]):
                        wszyscy_na_miejscu[i]='falsz'
            if(wszyscy_na_miejscu[i]=='falsz'):
                los = np.random.randint(0, 2)
                if (los == 0):
                    los = -1
                while(tabela_wspolrzednych_ludzi[i][1]+los<1 or tabela_wspolrzednych_ludzi[i][1]+los>X):
                    los = np.random.randint(0, 2)
                    if (los == 0):
                        los = -1
                tabela_wspolrzednych_ludzi[i][1] = tabela_wspolrzednych_ludzi[i][1]+los
        else:
            wszyscy_na_miejscu[i]='falsz'
            tabela_wspolrzednych_ludzi[i][1]=tabela_wspolrzednych_ludzi[i][1]+tabela_wektorow[i][0]/abs(tabela_wektorow[i][0]) # poruszanie się o 1 pole w kierunku wybranej osoby (w osi X)
            for otaa in range(L):
                if(otaa!=i):
                    if(tabela_wspolrzednych_ludzi[i][1] == tabela_wspolrzednych_ludzi[otaa][1]):
                        wszyscy_na_miejscu[i]='else_falsz'
            if(wszyscy_na_miejscu[i]=='else_falsz'):
                los = np.random.randint(0, 2)
                if (los == 0):
                    los = -1
                while(tabela_wspolrzednych_ludzi[i][1]+los<1 or tabela_wspolrzednych_ludzi[i][1]+los>X):
                    los = np.random.randint(0, 2)
                    if (los == 0):
                        los = -1
                tabela_wspolrzednych_ludzi[i][1] = tabela_wspolrzednych_ludzi[i][1]+los
                wszyscy_na_miejscu[i]='falsz'

        if (tabela_wspolrzednych_ludzi[tabela_wyboru[i][1] - 1][2]-2 < tabela_wspolrzednych_ludzi[i][2] < tabela_wspolrzednych_ludzi[tabela_wyboru[i][1] - 1][2]+2):
            wszyscy_na_miejscu[i] = 'prawda'
            for otaa in range(L):
                if(otaa!=i):
                    if(tabela_wspolrzednych_ludzi[i][2] == tabela_wspolrzednych_ludzi[otaa][2]):
                        wszyscy_na_miejscu[i]='falsz'
            if(wszyscy_na_miejscu[i]=='falsz'):
                los = np.random.randint(0, 2)
                if (los == 0):
                    los = -1
                while(tabela_wspolrzednych_ludzi[i][2]+los<1 or tabela_wspolrzednych_ludzi[i][2]+los>Y):
                    los = np.random.randint(0, 2)
                    if (los == 0):
                        los = -1
                tabela_wspolrzednych_ludzi[i][2] = tabela_wspolrzednych_ludzi[i][2]+los
        else:
            wszyscy_na_miejscu[i]='falsz'
            tabela_wspolrzednych_ludzi[i][2]=tabela_wspolrzednych_ludzi[i][2]+tabela_wektorow[i][1]/abs(tabela_wektorow[i][1]) # poruszanie się o 1 pole w kierunku wybranej osoby (w osi Y)
            for otaa in range(L):
                if(otaa!=i):
                    if(tabela_wspolrzednych_ludzi[i][2] == tabela_wspolrzednych_ludzi[otaa][2]):
                        wszyscy_na_miejscu[i]='else_falsz'
            if(wszyscy_na_miejscu[i]=='else_falsz'):
                los = np.random.randint(0, 2)
                if (los == 0):
                    los = -1
                while(tabela_wspolrzednych_ludzi[i][2]+los<1 or tabela_wspolrzednych_ludzi[i][2]+los>Y):
                    los = np.random.randint(0, 2)
                    if (los == 0):
                        los = -1
                tabela_wspolrzednych_ludzi[i][2] = tabela_wspolrzednych_ludzi[i][2]+los
                wszyscy_na_miejscu[i] = 'falsz'

    wszyscy_na_miejscu_lol = 'prawda'
    for lol in range(L):
        if (wszyscy_na_miejscu[lol]=='falsz'):
            wszyscy_na_miejscu_lol='falsz'

    # odtworzenie tabeli rozmieszczenia ludzi / stworzenie końcowej tabeli rozmieszczenia ludzi
    pole = [['' for x in range(X)] for y in range(Y)]
    for y in range(Y):
        for x in range(X):
            for lp in range(L):
                if (tabela_wspolrzednych_ludzi[lp][1] - 1 == x):
                    if (tabela_wspolrzednych_ludzi[lp][2] - 1 == y):
                        pole[y][x] = str(lp+1)

    # odswiez_ekran()
    # poczekaj(3000)
    # k += 1
    # print("Pole po przetasowaniu nr.:" + str(k))
    # print(np.matrix(pole))
    # print("\n")


print("Pole po ostatecznym przetasowaniu:")
print(np.matrix(pole))
print("\n")
print("Tabela współrzędnych ludzi po przetasowaniu:")
print(np.matrix(tabela_wspolrzednych_ludzi))
print("\n")

input("Wciśnij cokolwiek, aby zakończyć program.")