hamburger = ['Hamburger', 15.99]
cheeseburger = ['Cheeseburger', 17.99]
bekonburger = ['Bekon Burger', 21.99]
podwbekburger = ['Podwójny Bekon Burger', 27.99]
frytkiXXL = ['Frytki XXL', 8.99]
frytkimale = ['Frytki klasyczne', 4.99]
krazkiceb = ['Krążki cebulowe 9 szt.', 7.99]
cola_05 = ['Coca-Cola 0,5', 5.99]
fanta_05 = ['Fanta', 5.99]

cale_zamowienie = []
suma_zamowienia = []


def dodaj_do_zamowienia(produkt):
    cale_zamowienie.append(produkt)
    suma_zamowienia.append(produkt[1])
    print('Dodano do zamówienia: ', produkt[0])


imię = input('Jak masz na imię? ')
print()
print('Cześć', imię, '!')

while True:
    print()
    print('0. Zakończ')
    print('1. Burger Queen Opole')
    print('2. Burger Queen Katowice Galeria')
    print('3. Burger Queen Warszawa Mokotów')
    print('4. Burger Queen Warszawa Śródmieście')
    print('5. Burger Queen Wrocław Rynek')
    restauracja = int(input('Wybierz swoją restaurację: '))

    if restauracja == 0:
        print('Dziękujemy za skorzystanie z aplikacji Burger Queen')
        break
    if restauracja == 1:
        print('Twoja restauracja to Burger Queen Opole')
        while True:
            print()
            print('0. Powrót do wyboru restauracji')
            print('1. Burgery')
            print('2. Frytki')
            print('3. Przekąski')
            print('4. Napoje')
            print('5. Pokaż moje zamówienie')
            print('6. Do kasy')
            kategoria = int(input('Wybierz kategorię z menu: '))

            if kategoria == 0:
                break
            if kategoria == 1:
                print()
                print('Burgery')
                while True:
                    print('0. Powrót do wyboru kategorii')
                    print('1. Hamburger')
                    print('2. Cheeseburger')
                    print('3. Bekon Burger')
                    print('4. Podwójny Bekon Burger')
                    wybrany_produkt = int(input('Wybierz produkt: '))

                    if wybrany_produkt == 0:
                        break
                    if wybrany_produkt == 1:
                        dodaj_do_zamowienia(hamburger)
                    if wybrany_produkt == 2:
                        dodaj_do_zamowienia(cheeseburger)
                    if wybrany_produkt == 3:
                        dodaj_do_zamowienia(bekonburger)
                    if wybrany_produkt == 4:
                        dodaj_do_zamowienia(podwbekburger)

            if kategoria == 2:
                print()
                print('Frytki')
                while True:
                    print('0. Powrót do wyboru kategorii')
                    print('1. Frytki XXL')
                    print('2. Frytki klasyczne')
                    wybrany_produkt = int(input('Wybierz produkt: '))

                    if wybrany_produkt == 0:
                        break
                    if wybrany_produkt == 1:
                        dodaj_do_zamowienia(frytkiXXL)
                    if wybrany_produkt == 2:
                        dodaj_do_zamowienia(frytkimale)

            if kategoria == 3:
                print()
                print('Przekąski')
                while True:
                    print('0. Powrót do wyboru kategorii')
                    print('1. Krążki cebulowe')
                    wybrany_produkt = int(input('Wybierz produkt: '))

                    if wybrany_produkt == 0:
                        break
                    if wybrany_produkt == 1:
                        dodaj_do_zamowienia(krazkiceb)

            if kategoria == 4:
                print()
                print('Napoje')
                while True:
                    print('0. Powrót do wyboru kategorii')
                    print('1. Coca-Cola 0,5')
                    print('2. Fanta 0,5')
                    wybrany_produkt = int(input('Wybierz produkt: '))

                    if wybrany_produkt == 0:
                        break
                    if wybrany_produkt == 1:
                        dodaj_do_zamowienia(cola_05)
                    if wybrany_produkt == 2:
                        dodaj_do_zamowienia(fanta_05)

            if kategoria == 5:
                print()
                print('Twoje zamówienie: ', cale_zamowienie)
                print('Kwota zamówienia: ', sum(suma_zamowienia), 'zł')
                while True:
                    print()
                    powrot = int(input("Wciśnij '1', by wrócić do menu: "))

                    if powrot == 1:
                        break

            if kategoria == 6:
                print()
                print('Twoje zamówienie: ', cale_zamowienie)
                print('Kwota zamówienia: ', sum(suma_zamowienia), 'zł')
                while True:
                    print()
                    print('0. Powrót do wyboru kategorii')
                    print('1. Zapłać')
                    platnosc = int(input('To już wszystko?: '))

                    if platnosc == 0:
                        break
                    if platnosc == 1:
                        break

    if restauracja == 2:
        print('Twoja restauracja to Burger Queen Katowice Galeria')
    if restauracja == 3:
        print('Twoja restauracja to Burger Queen Warszawa Mokotów')
    if restauracja == 4:
        print('Twoja restauracja to Burger Queen Warszawa Śródmieście')
    if restauracja == 5:
        print('Twoja restauracja to Burger Queen Wrocław Rynek')
