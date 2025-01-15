##Sofia Frontalini
#Classe 4BS
#Classe Moto

from veicolo import Veicolo

class Moto(Veicolo):
    def __init__(self, targa : str, numeroMaxPasseggeri: int, numeroPasseggeriTrasportati : int, maxCapacitàTrasporto : int):
        super().__init__(targa)
        if numeroMaxPasseggeri <= 0 or numeroMaxPasseggeri >= 3:
            raise ValueError ("Non è possibile")
        else:
            self.__numeroMaxPasseggeri = numeroMaxPasseggeri
        if numeroPasseggeriTrasportati > numeroMaxPasseggeri:
            raise ValueError ("Non è possibile")
        else:
            self.__numeroPasseggeriTrasportati = numeroPasseggeriTrasportati
        self.__maxCapacitàTrasporto = maxCapacitàTrasporto
   
    @property
    def numeroMaxPasseggeri(self):
        return numeroMaxPasseggeri
    
    @property
    def numeroPasseggeriTrasportati(self):
        return numeroPasseggeriTrasportati
    
    @property
    def maxCapacitàTrasporto(self):
        return maxCapacitàTrasporto
    
    @numeroMaxPasseggeri.setter
    def numeroMaxPasseggeri(self, value):
        if value <= 0 and value >= 3:
            raise ValueError ("Non è possibile")
        self.__numeroMaxPasseggeri = value
        return
    
    @numeroPasseggeriTrasportati.setter
    def numeroPasseggeriTrasportati(self, value):
        if value > numeroMaxPasseggeri:
            raise ValueError ("Non è possibile")
        self.__numeroPasseggeriTrasportati = value
        return
    
    @maxCapacitàTrasporto.setter
    def maxCapacitàTrasporto(self, value):
        self.__maxCapacitàTrasporto = value
        return
    
if "__main__" == __name__:
    m1 = Moto("XW 491 JR", 2, 2, 400)
    print(m1)
#     m2 = Moto("XP 491 JR", 4, 2, 400)
#     print(m2)
