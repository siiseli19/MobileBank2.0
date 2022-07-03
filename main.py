#driver code for the application


from datetime import date

#starting screen for the app
def starting_creen():
    pass


#vaihda lontooksi
def user_interface():

    valinta = None
    while True:
        print("-------------------------------------------")
        print("Tervetuloa kayttamaan mobiilipankkia!")
        saldo()
        print("VALITSE TOIMINTO:")
        print("Tilisiirto -- S")
        print("Tilitapahtumat -- T")
        print("Hae lainaa -- H")
        print("Poistu -- Q")
        print("Seuraa kulutsta -- K")
        print("-------------------------------------------")

        try:
            valinta = str(input().upper())

            if valinta == "S":
                saaja = input("Syota maksun saajan nimi")
                summa = float(input("Syota siirrettava summa"))
                pvm = date.today()

        except:
            print('Something went wrong')

