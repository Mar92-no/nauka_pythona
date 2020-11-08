# imie  = 'Ala'
# zwierze = 'kot'
# ile = 5
#
# if ile ==1:
#     print ('{0} ma {1}a' .format(imie, zwierze))
# else:
#     print ('{0} ma {1}ow' .format(imie, zwierze))

marka = 'toyota'
pojemnosc = 1.0

ile = marka.count('o')

if ile == 1:
    print ("Samochod marki {0} o pojemnosci {1}, ma jedna litere -a- w nazwie" .format(marka, pojemnosc))
else:
    print ("Samochod marki {0} o pojemnosci {1}, ma {2} -a- w nazwie" .format(marka, pojemnosc, ile))
