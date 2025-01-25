#Sofia Frontalini
#Classe 4BS
#Esercizio

from postoMezzo import PostoMezzo
from veicolo import Veicolo
from auto import Auto
from moto import Moto
listaAuto = ["FIAT", "FERRARI", "AUDI", "BMW", "MASERATI", "VOLKSWAGEN", "ALFA ROMEO", "MERCEDES"]
listaMoto = ["FANTIC", "BETA", "E-SCOOTER", "HARLEY-DAVIDSON"]

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
    
#     def parcheggia(self, veicolo:Veicolo):
#         if veicolo.marca in listaAuto:
#             # allora è un auto...
#             for posto in self.__postiAuto:
#                 if not posto.occupato():
#                     posto.occupaPosto(veicolo.targa)
#                     return True
#                 
#                 # posti auto pieni
#                 return False
#         
#         if veicolo.marca in listaMoto:
#             # allora è un moto...
#             for posto in self.__postiMoto:
#                 if not posto.occupato():
#                     posto.occupaPosto(veicolo.targa)
#                     return True
#             
#             # posti moto pieni
#             return False
#     
#     def libera(self, veicolo: Veicolo):
#         if veicolo.marca in listaAuto:
#             # allora è un auto...
#             for posto in self.__postiAuto:
#                 posto.liberaPosto(veicolo.targa)
#                 numeroOre = (posto.dataFineParcheggio - posto.dataInizioParcheggio).total_seconds() / 3600
#                 saldo = numeroOre * 1.5
#                 self.__guadagno += saldo
#                 return True
#             
#             return False
#         
#         if veicolo.marca in listaMoto:
#             # allora è un auto...
#             for posto in self.__postiMoto:
#                 posto.liberaPosto(veicolo.targa)
#                 numeroOre = (posto.dataFineParcheggio - posto.dataInizioParcheggio).total_seconds() / 3600
#                 saldo = numeroOre * 1.2
#                 self.__guadagno += saldo
#                 return True
#             
#             return False

    def parcheggia(self, marcaVeicolo, targaVeicolo):
        if marcaVeicolo in listaAuto:
            # allora è un auto...
            for posto in self.__postiAuto:
                if not posto.occupato():
                    posto.occupaPosto(targaVeicolo)
                    return True
                
                # posti auto pieni
                return False
        
        if marcaVeicolo in listaMoto:
            # allora è un moto...
            for posto in self.__postiMoto:
                if not posto.occupato():
                    posto.occupaPosto(targaVeicolo)
                    return True
            
            # posti moto pieni
            return False
    
#     def libera(self, marcaVeicolo, targaVeicolo):
#         if marcaVeicolo in listaAuto:
#             # allora è un auto...
#             for posto in self.__postiAuto:
#                 posto.liberaPosto(targaVeicolo)
#                 numeroOre = (posto.dataFineParcheggio - posto.dataInizioParcheggio).total_seconds() / 3600
#                 saldo = numeroOre * 1.5
#                 self.__guadagno += saldo
#                 return True
#             
#             return False
#         
#         if marcaVeicolo in listaMoto:
#             # allora è un auto...
#             for posto in self.__postiMoto:
#                 posto.liberaPosto(targaVeicolo)
#                 numeroOre = (posto.dataFineParcheggio - posto.dataInizioParcheggio).total_seconds() / 3600
#                 saldo = numeroOre * 1.2
#                 self.__guadagno += saldo
#                 return True
#             
#             return False
            
    
    def scrittura(self):
        from pathlib import Path
        import csv
        #si crea un nuovo file
        #crea la cartella ovunque essa sia
        nuovoFile = Path.cwd() / "park.data"
        fileParcheggio = nuovoFile.open("w")
        campi = ["_PostoMezzo__targa", "_PostoMezzo__dataInizioParcheggio", "_PostoMezzo__dataFineParcheggio"]

        scrittore = csv.DictWriter(fileParcheggio, campi)
        scrittore.writeheader()
    
        for riga in self.__postiAuto:
            scrittore.writerow(riga)
            
        for riga in self.__postiMoto:
            scrittore.writerow(riga)
            
        scrittore.writerow(self.__guadagno)
    
        fileParcheggio.close()
        return
            
                
if __name__ == "__main__":
    p = Parcheggio()
    print(p)
    auto1 = p.parcheggia("FERRARI", "AS 234 DE")
    print(auto1)
    moto1 = p.parcheggia("FANTIC", "TR 892 OI")
    print(moto1)
#     auto1l = p.libera("FERRARI", "AS 234 DE")
#     print(auto1l)
    print(p)
    
    print(p.scrittura())
    
