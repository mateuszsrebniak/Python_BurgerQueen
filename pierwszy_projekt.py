imię = input('Jak masz na imię? ')
print()
print('Cześć', imię,'!')

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
                    wybrany_produkt1 = int(input('Wybierz produkt: '))

                    if wybrany_produkt1 == 0:
                        break
        
            if kategoria == 2:
                print()
                print('Frytki')
                while True:
                    print('0. Powrót do wyboru kategorii')
                    print('1. Frytki XXL')
                    print('2. Frytki klasyczne')
                    wybrany_produkt2 = int(input('Wybierz produkt: '))

                    if wybrany_produkt2 == 0:
                        break

            if kategoria == 3:
                print()
                print('Przekąski')
                while True:
                    print('0. Powrót do wyboru kategorii')
                    print('1. Krążki cebulowe')
                    wybrany_produkt3 = int(input('Wybierz produkt: '))

                    if wybrany_produkt3 == 0:
                        break

            if kategoria == 4:
                print()
                print('Napoje')
                while True:
                    print('0. Powrót do wyboru kategorii')
                    print('1. Coca-Cola 0,5')
                    print('2. Fanta 0,5')
                    wybrany_produkt4 = int(input('Wybierz produkt: '))

                    if wybrany_produkt4 == 0:
                        break
            
    if restauracja == 2:
        print('Twoja restauracja to Burger Queen Katowice Galeria')
    if restauracja == 3:
        print('Twoja restauracja to Burger Queen Warszawa Mokotów')
    if restauracja == 4:
        print('Twoja restauracja to Burger Queen Warszawa Śródmieście')
    if restauracja == 5:
        print('Twoja restauracja to Burger Queen Wrocław Rynek')
