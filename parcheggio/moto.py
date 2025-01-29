##Sofia Frontalini
#Classe 4BS
#Classe Moto

#importo la classe Veicolo dal file veicolo
from veicolo import Veicolo

#Classe Moto ereditata da Veicolo
class Moto(Veicolo):
    #funzione iniziale con attributi quali marca, targa, numero massimo di passeggeri, numero di passeggeri trasportati e il massimo della capacità di trasporto
    def __init__(self, marca : str, targa : str, numeroMaxPasseggeri: int, numeroPasseggeriTrasportati : int, maxCapacitàTrasporto : int):
        super().__init__(marca, targa)
        
        #controllo che il numero massimo di passeggeri sia compreso tra 0 e 3 esclusi
        #in caso contrario ritorna errore
        if numeroMaxPasseggeri <= 0 or numeroMaxPasseggeri >= 3:
            raise ValueError ("Non è possibile")
        else:
            self.__numeroMaxPasseggeri = numeroMaxPasseggeri
            
        #controllo che il numero di passegeri trasportati sia minore del numero massimo di passeggeri 
        #in caso contrario ritorna errore
        if numeroPasseggeriTrasportati > numeroMaxPasseggeri:
            raise ValueError ("Non è possibile")
        else:
            self.__numeroPasseggeriTrasportati = numeroPasseggeriTrasportati
            
        self.__maxCapacitàTrasporto = maxCapacitàTrasporto
   
    #imposto le proprietà su numeroMaxPasseggeri, numeroPasseggeriTrasportati e maxCapacitàTrasporto
    @property
    def numeroMaxPasseggeri(self):
        return self.__numeroMaxPasseggeri
    
    @property
    def numeroPasseggeriTrasportati(self):
        return self.__numeroPasseggeriTrasportati
    
    @property
    def maxCapacitàTrasporto(self):
        return self.__maxCapacitàTrasporto
    
    #imposto le setter
    
#     #è possibile cambiare il numero massimo di passeggeri se è compreso tra 0 e 3 esclusi sennò ritorna errore
#     @numeroMaxPasseggeri.setter
#     def numeroMaxPasseggeri(self, value):
#         if value <= 0 and value >= 3:
#             raise ValueError ("Non è possibile")
#         self.__numeroMaxPasseggeri = value
#         return
    
    #è possibile cambiare  il numero di passegeri trasportati se è minore del numero massimo di passeggeri sennò ritorna errore
    @numeroPasseggeriTrasportati.setter
    def numeroPasseggeriTrasportati(self, value):
        if value > numeroMaxPasseggeri:
            raise ValueError ("Non è possibile")
        self.__numeroPasseggeriTrasportati = value
        return
    
    #è possibile cambiare maxCapacitàTrasporto
    @maxCapacitàTrasporto.setter
    def maxCapacitàTrasporto(self, value):
        self.__maxCapacitàTrasporto = value
        return

#I TEST
if "__main__" == __name__:
    m1 = Moto("HARLEY-DAVIDSON", "XW 491 JR", 2, 2, 400)
    print(m1)
    
#     m2 = Moto("XP 491 JR", 4, 2, 400)
#     print(m2)
