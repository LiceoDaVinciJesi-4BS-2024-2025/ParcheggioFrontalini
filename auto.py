##Sofia Frontalini
#Classe 4BS
#Classe Auto

from veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, targa : str, numeroMaxPasseggeri: int, numeroPasseggeriTrasportati : int, maxCapacitàTrasporto : int):
        super().__init__(targa)
        if numeroMaxPasseggeri <= 0 or numeroMaxPasseggeri >= 9:
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
        if value <= 0 and value >= 9:
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
    a1 = Auto("QW 562 QB", 4, 2, 10000)
    print(a1)
#     a2 = Auto("QW 592 QB", 9, 2, 10000)
#     print(a2)