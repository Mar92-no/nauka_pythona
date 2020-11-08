koszyk_items = ['mleko', 'czekolada', 'sok', 'piwo']
koszyk_ilosc = [2, 1, 3]
koszyk_cena_items = [30, 40, 20, 6]

suma = 0.0
for idx in range(len(koszyk_items)):
    items = koszyk_items[idx]
    ile = koszyk_ilosc[idx]
    cena = koszyk_cena_items[idx]* ile
    print("{0} {1} {2}" .format(items, ile, cena))
    suma = suma + cena

print("Wartosc koszyka {0} przed znizka" .format(suma))

# if 'mleko' in koszyk_items and 'czekolada' in koszyk_items:
#     print('Hurra! Znizka!')
#     suma = suma - (suma * 10)/100

znizka_r1 = 0

if len(koszyk_items) > 3: #R1
    suma = suma - (suma*5)/100
    znizka_r1 = 1

if suma >= 500 and znizka_r1 == 0:           #R2
    suma = suma - (suma*10)/100

print("Wartosc koszyka {0} po znizce" .format(suma))
