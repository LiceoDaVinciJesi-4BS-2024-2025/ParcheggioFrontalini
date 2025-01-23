#Sofia Frontalini
#Classe 4BS
#Esercizio

from postoMezzo import PostoMezzo
from veicolo import Veicolo
from auto import Auto
from moto import Moto
listaAuto = ["FIAT", "FERRARI", "AUDI", "BMW", "MASERATI", "VOLKSWAGEN", "ALFA ROMEO", "MERCEDES"]

class Parcheggio:
    def __init__(self):
        self.__postiAuto=[]
        for n in range(1000):
            posto = PostoMezzo()
            self.__postiAuto.append(posto)
        
        self.__postiMoto = []
        for n in range(200):
            posto = PostoMezzo()
            self.__postiMoto.append(posto)
            
        self.__guadagno = 0
            
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)
    
    def parcheggia(self, veicolo:Veicolo):
        if isinstance(veicolo, Auto):
            # allora è un auto...
            for posto in self.__postiAuto:
                if not posto.occupato():
                    posto.occupaPosto(veicolo.targa)
                    return True
            
            # posti auto pieni
            return False
        
        if isinstance(veicolo, Moto):
            # allora è un moto...
            for posto in self.__postiMoto:
                if not posto.occupato():
                    posto.occupaPosto(veicolo.targa)
                    return True
            
            # posti moto pieni
            return False
    
    def libera(self, veicolo: Veicolo):
        if isinstance(veicolo, Auto):
            # allora è un auto...
            for posto in self.__postiAuto:
                posto.liberaPosto(veicolo.targa)
                numeroOre = (posto.dataFineParcheggio - posto.dataInizioParcheggio).total_seconds() / 3600
                saldo = numeroOre * 1.5
                self.__guadagno += saldo
                return True
            
            return False
        
        if isinstance(veicolo, Moto):
            # allora è un auto...
            for posto in self.__postiMoto:
                posto.liberaPosto(veicolo.targa)
                numeroOre = (posto.dataFineParcheggio - posto.dataInizioParcheggio).total_seconds() / 3600
                saldo = numeroOre * 1.2
                self.__guadagno += saldo
                return True
            
            return False
                
                
if __name__ == "__main__":
    p = Parcheggio()
    print(p)
    auto1 = p.parcheggia("AS 234 DE")
    print(auto1)
        
