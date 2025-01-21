#Sofia Frontalini
#Classe 4BS
#Esercizio

#1000 auto e 200 moto
from auto import Auto
from moto import Moto

class Parcheggio:
    
    def __init__(self, nomeParcheggio):
        self.__nomeParcheggio = nomeParcheggio
        self.__postiLiberiAuto = 1000
        self.__postiLiberiMoto = 200
        
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)
    
    @property
    def nomeParcheggio(self):
        return nomeParcheggio
    
    @property
    def postiLiberiAuto(self):
        return postiLiberiAuto
    
    @property
    def postiLiberiMoto(self):
        return postiLiberiMoto