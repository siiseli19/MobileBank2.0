#driver code for the application
from functions import show_balance, show_payment_history

from datetime import date

#starting screen for the app
def starting_creen():
    pass


#vaihda lontooksi
def user_interface():

    valinta = None
    while True:
        print("Welcome to MobileBank")
        print("-------------------------------------------")
        show_balance()
        print("-------------------------------------------")

        try:
            valinta = str(input().upper())

            if valinta == "S":
                saaja = input("Syota maksun saajan nimi")
                summa = float(input("Syota siirrettava summa"))
                pvm = date.today()

        except:
            print('Something went wrong')

