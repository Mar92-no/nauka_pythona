# produkt = {'SS12': 'sukienka', 'P12': 'spodnie'}
#
# igla = 'P12'
#
# if 'P12' in produkt:
#     print('istnieje!')
#     print(produkt['P12'])

# produkt = {
#  'SS12': {'nazwa': 'sukienka', 'rozmiary': ['s', 'xl']},
#  'P12': {'nazwa': 'spodnie', 'rozmiary': ['s', 'xl']}
#  }
#
# # for p in produkt:
# #     print(p)
#
# for id in produkt:
#     p = produkt[id]
#     print(p)
#     print(p['nazwa'])
#
# # igla = 'P12'
# #
# # if 'P12' in produkt:
# #     print('istnieje!')
# #     print(produkt['P12'])
# #

elementy = {
'S1': {'warzywo': 'pomidor', 'cena': ['4zl','2zl']},
'S2': {'warzywo': 'ogorek', 'cena': ['1zl','2zl']}
}

for id in elementy:
    p = elementy[id]
    print(p['warzywo'])
    cena = p['cena']
    for c in cena:
        print(c)
