import CRUD_MODULE

text = ' \nWybór zadań : \n(1) Wczytaj rekordy z pliku (CREATE) \n(2) Wpisz rekordy w konsoli (CREATE) \n(3) Odczytaj zawartość bazy (READ) \n(4) Zmiana rekordu (UPDATE) \n(5) Usuń rekord (DELETE) \n(6) Średni wiek (D1) \n(7) K/M (D2)'
def Wybor_Zadan(i):
    print(text)
    x = input()

    if x == '1':
        path = input("Podaj nazwe pliku : ")
        CRUD_MODULE.LoadToDataBaseFromFile(path, i)
        Wybor_Zadan(2)
    elif x == '2':
        k = input("Podaj indeks : ")
        r_imie = input("Podaj imie : ")
        r_nazwisko = input("Podaj nazwisko : ")
        r_pesel = input("Podaj pesel : ")
        CRUD_MODULE.LoadToDataBaseFromConsole(i, k , r_imie, r_nazwisko, r_pesel)
        Wybor_Zadan(2)
    elif x == '3':
        CRUD_MODULE.PrintFromDataBase()
        Wybor_Zadan(2)
    elif x == '4':
        index = input("Podaj nr.indeksu : ")
        CRUD_MODULE.UpdateDataBase(index)
        Wybor_Zadan(2)
    elif x == '5':
        index = input("Podaj nr.indeksu : ")
        CRUD_MODULE.DeleteFromDataBase(index)
        Wybor_Zadan(2)
    elif x == '6':
        CRUD_MODULE.AgeFromDataBase()
        Wybor_Zadan(2)
    elif x == '7':
        CRUD_MODULE.FemaleMaleDataBase()
        Wybor_Zadan(2)
    else:
        print('Wprowadziłeś niepoprawną wartość , spróbuj ponownie:')
        Wybor_Zadan()
Wybor_Zadan(1)