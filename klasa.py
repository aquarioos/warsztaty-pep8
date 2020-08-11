from eratostenes_lib import eratostenes

class mojaKlasa:
    def __init__(self, gornyZakres = 137):
        
        self.__gorny_zakres = gornyZakres
    def CalcPrimes(self, inny_zakres= None):
        if inny_zakres:
            return eratostenes(inny_zakres)
        else:
            return eratostenes(self.__gorny_zakres)

moja_klasa = mojaKlasa(gornyZakres=192)

l_pierwsze_do_100 = moja_klasa.CalcPrimes(100)
print('[INFO] liczby pierwsze do 100: {}'.format(', '.join(map(str, l_pierwsze_do_100))))
l_pierwsze_do_1000 = moja_klasa.CalcPrimes(1000)
print('[INFO] liczby pierwsze do 100: {}'.format(', '.join(map(str, l_pierwsze_do_1000))))