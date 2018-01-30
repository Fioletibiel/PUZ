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
def int2float_2(tabela):
    for li in range(L):
        for i in range(2):
            tabela[li][i] = float(tabela[li][i])
def int2float_3(tabela):
    for li in range(L):
        for i in range(3):
            tabela[li][i] = float(tabela[li][i])
def float2int_2(tabela):
    for li in range(L):
        for i in range(2):
            tabela[li][i] = float(tabela[li][i])
def float2int_3(tabela):
    for li in range(L):
        for i in range(3):
            tabela[li][i] = float(tabela[li][i])

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
    tabela_wyboru[l] = [l+1,np.random.randint(0,L)+1]
    while(tabela_wyboru[l][1]==tabela_wyboru[l][0]):
        tabela_wyboru[l] = [l+1, np.random.randint(0,L)+1]
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
# print("Tabela współrzędnych ludzi:")
# print(np.matrix(tabela_wspolrzednych_ludzi))
# print("\n")

# symulacja ruchu ludzi
tabela_celu = [[0 for i in range(2)] for l in range(L)]
tabela_wektorow = [[0 for i in range(2)] for l in range(L)]
tabela_ruchu = [[0 for i in range(2)] for l in range(L)]
int2float_2(tabela_ruchu)
int2float_2(tabela_wektorow)
int2float_3(tabela_wspolrzednych_ludzi)
k=0
while(tabela_wspolrzednych_ludzi!=tabela_celu):
    for i in range(L):
        tabela_wektorow[i][0] = tabela_wspolrzednych_ludzi[tabela_wyboru[i][1]-1][1] - 1 - (tabela_wspolrzednych_ludzi[i][1] - 1) - 1 # przesunięcie w osi X
        tabela_wektorow[i][1] = tabela_wspolrzednych_ludzi[tabela_wyboru[i][1]-1][2] - 1 - (tabela_wspolrzednych_ludzi[i][2] - 1) - 1 # przesunięcie w osi Y
        tabela_celu[i][0] = tabela_wspolrzednych_ludzi[i][1] + tabela_wektorow[i][0]
        tabela_celu[i][1] = tabela_wspolrzednych_ludzi[i][2] + tabela_wektorow[i][1]
        # tabela_wektorow_bufor = tabela_wektorow
        # for lo in range(L):
        #     if(tabela_wektorow_bufor[lo][0]<0):
        #         tabela_wektorow_bufor[lo][0]=tabela_wektorow_bufor[lo][0]*(-1)
        #     if(tabela_wektorow_bufor[lo][1]<0):
        #         tabela_wektorow_bufor[lo][1] = tabela_wektorow_bufor[lo][1]*(-1)
        # ilosc_okresow = np.min(tabela_wektorow_bufor)
        # if (ilosc_okresow==0):
        #     ilosc_okresow = 1
        tabela_ruchu[i][0] = tabela_wspolrzednych_ludzi[i][1] + tabela_wektorow[i][0]#/ilosc_okresow
        tabela_ruchu[i][1] = tabela_wspolrzednych_ludzi[i][2] + tabela_wektorow[i][1]#/ilosc_okresow
        float2int_2(tabela_ruchu)
        tabela_wspolrzednych_ludzi[i][1] = tabela_ruchu[i][0]
        tabela_wspolrzednych_ludzi[i][2] = tabela_ruchu[i][1]
        float2int_3(tabela_wspolrzednych_ludzi)
    # odtworzenie tabeli rozmieszczenia ludzi / stworzenie końcowej tabeli rozmieszczenia ludzi
    pole = [['' for x in range(X)] for y in range(Y)]
    for y in range(Y):
        for x in range(X):
            for lp in range(L):
                if (tabela_wspolrzednych_ludzi[lp][1] - 1 == x):
                    if (tabela_wspolrzednych_ludzi[lp][2] - 1 == y):
                        pole[y][x] = '©'
    odswiez_ekran()
    poczekaj(2)
    k += 1
    print("Pole po przetasowaniu nr.:" + str(k))
    print(np.matrix(pole))
    print("\n")
    if (k == 5):
        break
input("Wciśnij cokolwiek, aby zakończyć program.")