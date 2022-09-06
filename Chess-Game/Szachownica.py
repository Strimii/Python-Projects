import random


plansza = [ [ ' - ' for _ in range(8) ] for _ in range(8) ]
kolizje_hetmani = []
figury = []
Zbior_Figur = [' P ', ' H ', ' H ']
# H - Hetman P - Pion
text = '\nDziałanie się zakończyło. Masz możliwość wyboru dodatkowych opperacji \n (1) Wylosuj nową pozycję dla pionka \n (2) Usuń dowolnego hetmana \n (3) Zakończ program'

def Rysuj_Plansze():

    for rzad in range(0, 9):
        x = ''
        if rzad == 0:
            for kolumna in range(0, 9):
                if kolumna == 0:
                    x += f"\n   "
                    continue
                x += f" {kolumna-1} "
        else:
            for pola in range(0, 9):
                if pola == 0:
                    x += f" {rzad-1} "
                else:
                    x += plansza[pola-1][rzad-1]
        print(x)


def Tworzenie_Figur(first):
    if (first == 1):
        i = 0
        for nazwa in Zbior_Figur:
            i += 1
            figury.append({'Figura': nazwa, 'Y': random.randint(1, 7), 'X': random.randint(1, 7), 'i': i})
    ok = 1
    for sprawdz_figury in figury:
        for sprawdz_figury2 in figury:
            if (sprawdz_figury['i'] == sprawdz_figury2['i']):
                continue
            if (sprawdz_figury['X'] == sprawdz_figury2['X'] and sprawdz_figury['Y'] == sprawdz_figury2['Y']):
                ok = 0
    if (ok == 0):
        if(first == 1):
            figury.clear()
            Tworzenie_Figur()
        if(first == 2):
            Losuj_Piona()


def Rozmieszczanie_Figur():
    for figura in figury:
        # Parametry figury
        nazwa = figura['Figura']
        y = figura['Y']
        x = figura['X']
        plansza[x][y] = nazwa

def Sprawdz_Kolizje():
    # parametry piona
    pionY = figury[0]['Y']
    pionX = figury[0]['X']
    kolizje_hetmani.clear()
    for figura in figury:
        if(figura['Figura'] != ' P '):
            # bicie w pionie i poziomie
            if(figura['Y'] == pionY or figura['X'] == pionX):
                kolizje_hetmani.append((figura['X'], figura['Y'] ))
                break

            # Sprawdza bicie na ukos
            for i in range(8):
                if(figura['X'] + i == pionX and figura['Y'] - i == pionY
                or figura['X'] + i == pionX and figura['Y'] + i == pionY
                or figura['X'] - i == pionX and figura['Y'] + i == pionY
                or figura['X'] - i == pionX and figura['Y'] - i == pionY):
                    kolizje_hetmani.append((figura['X'], figura['Y']))

    Wyniki_Bicia()
    print(text)
    Wybor_Zadan()
def Wyniki_Bicia():
    if(len(kolizje_hetmani) == 0):
        print("\nTwój pionek jest bezpieczny")
    else:
        print("\nHetmani którzy biją pion(X,Y): %s" % ", ".join(map(str, kolizje_hetmani)))

def Usun_Hetmana(x, y):
    plansza[x][y] = ' - '
    for figura in figury:
        if (figura['Y'] == y and figura['X'] == x):
            i = figury.index(figura)
            del figury[i]

def Losuj_Piona():

    for figura in figury:
        nazwa1 = figura['Figura']
        y1 = figura['Y']
        x1 = figura['X']
        if nazwa1 == Zbior_Figur[0]:
            plansza[x1][y1] = ' - '
            figury[0] = {'Figura': ' P ', 'Y': random.randint(1, 7), 'X': random.randint(1, 7), 'i': 1}

    Tworzenie_Figur(2)
    Rozmieszczanie_Figur()



def Wybor_Zadan():
    x = input()
    if x == '1':
        Losuj_Piona()
        Rysuj_Plansze()
        Sprawdz_Kolizje()

    elif x == '2':
        print('Podaj koordynaty hetmana do usunięcia')
        x_usun = int(input('X:'))
        y_usun = int(input('Y:'))
        Usun_Hetmana(x_usun, y_usun)
        Rysuj_Plansze()
        Sprawdz_Kolizje()

    elif x == '3':
        quit()
    else:
        print('Wprowadziłeś niepoprawną wartość , spróbuj ponownie:')
        Wybor_Zadan()

Tworzenie_Figur(1)
Rozmieszczanie_Figur()
Rysuj_Plansze()
Sprawdz_Kolizje()



















