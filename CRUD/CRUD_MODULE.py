DATA = []
DATA_keys = []
DATA_check = []

def LoadToDataBaseFromFile(path, i):
   # print(DATA_keys)

    if i == 1:
        File = open(path, 'r').read().split('\n')
        for line in File:
            DATA.append(line.split(';'))

      #  print(len(DATA))
        for keys in range(0, len(DATA)):
            DATA_keys.append(DATA[keys][0])
      #  print(DATA_keys)
    else:
        File = open(path, 'r').read().split('\n')
        for line in File:
            DATA_check.append(line.split(';'))
        ok = "ok"
        for check in DATA_keys:
            for keys_check in range(0, len(DATA_check)):
                if check == DATA_check[keys_check][0]:
                    print("Indeks z następującym numerem się powtarza - " + check)
                    ok = "not"
        if ok == "ok":
            for line in File:
                DATA.append(line.split(';'))
            for keys in range(0, len(DATA_check)):
                DATA_keys.append(DATA_check[keys][0])
         #   print(DATA_keys)
    DATA_check.clear()

def PrintFromDataBase():
    for element in DATA:
        print(element)

def LoadToDataBaseFromConsole(i, k , r_imie, r_nazwisko, r_pesel):
    dane = []
    dane.append(k)
    dane.append(r_imie)
    dane.append(r_nazwisko)
    dane.append(r_pesel)
    if i == 1:
        DATA_keys.append(k)
        DATA.append(dane)
    else:
        ok = "ok"
        for check in DATA_keys:
            if check == k:
                print("Indeks z następującym numerem się powtarza - " + check)
                ok = "not"
        if ok == "ok":
            DATA_keys.append(k)
            DATA.append(dane)

def UpdateDataBase(index):
    ok = "not"
    change = ""
    for count in range(0, len(DATA)):
        if DATA[count][0] == index:
            change = count
            ok = "ok"
    if ok == "not":
        print("Podany przez Ciebie indeks nie zawiera się w bazie")
    else:
        DATA[change][1] = input("Podaj nowe imie : ")
        DATA[change][2] = input("Podaj nowe nazwisko : ")
        DATA[change][3] = input("Podaj nowy pesel : ")

def DeleteFromDataBase(index):
    ok = "not"
    remove = ""
    for count in range(0, len(DATA)):
        if DATA[count][0] == index:
            remove = count
            ok = "ok"
    if ok == "not":
        print("Podany przez Ciebie indeks nie zawiera się w bazie")
    else:
        remove_key = ""
        for count_keys in range(0, len(DATA_keys)):
            if DATA_keys[count_keys] == index:
                remove_key = count_keys
        DATA.pop(remove)
        DATA_keys.pop(remove_key)

def FemaleMaleDataBase():
    Kobiety = 0
    Mezczyzni = 0
    for count in range(0, len(DATA)):
        Gender_check = DATA[count][3]
        check_r = Gender_check[9]
        if int(check_r) % 2 != 0:
            Mezczyzni += 1
        else:
            Kobiety += 1
    print("Kobiety : ")
    print(Kobiety)
    print("Mezczyzni : ")
    print(Mezczyzni)

def AgeFromDataBase():
        wiek = 0
        for count in range(0, len(DATA)):
            pesel = DATA[count][3]
            data_ur = 0
            if int(pesel[2]) == 8 or int(pesel[2]) == 9:
                data_ur = 1800
            elif int(pesel[2]) == 0 or int(pesel[2]) == 1:
                data_ur = 1900
            elif int(pesel[2]) == 2 or int(pesel[2]) == 3:
                data_ur = 2000
            data_ur = data_ur + int(pesel[0]) * 10 + int(pesel[1])
            wiek = wiek + 2021 - data_ur
        print(wiek / len(DATA))

