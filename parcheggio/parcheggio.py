#Sofia Frontalini
#Classe 4BS
#Esercizio

#1000 auto e 200 moto
from auto import Auto
from moto import Moto
from postoMezzo import PostoMezzo
import datetime

class Parcheggio:
    def __init__(self, nomeParcheggio):
        self.__nomeParcheggio = nomeParcheggio
        self.__postiLiberiAuto = 1000
        self.__postiLiberiMoto = 200
        self.__guadagnoParcheggio = 0
        
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
    
    def prenotazionePosto(self, mezzo: PostoMezzo):
        listaPrenotazionePosto = []
        if mezzo.tipologia == "auto":
            if self.__postiLiberiAuto > 0:
                numeroOreSosta = (mezzo.data - datetime.datetime.now()).total_seconds() / 3600 
                saldo = numeroOreSosta * 1.5
                listaPrenotazionePosto.append(mezzo.tipologia(), mezzo.targa(), numeroOreSosta, saldo)
                self.__postiLiberiAuto -= 1
                self.__guadagnoParcheggio += saldo
        elif mezzo.tipologia == "moto":
            if self.__postiLiberiMoto > 0:
                numeroOreSosta = (mezzo.data - datetime.datetime.now()).total_seconds() / 3600 
                saldo = numeroOreSosta * 1.2
                listaPrenotazionePosto.append(mezzo.tipologia(), mezzo.targa(), numeroOreSosta, saldo)
                self.__postiLiberiMoto -= 1
                self.__guadagnoParcheggio += saldo
        else:
            raise ValueError("Mezzo non valido")
        
        return listaPrenotazionePosto
    
if __name__ == "__main__":
    p = Parcheggio("Il mio Fantastico Parcheggio")
    print(p)
    prenotazione1 = p.prenotazionePosto(PostoMezzo("auto", "WE 369 PO", datetime.datetime(2025, 1, 21, 20, 18, 00)))
    print(prenotazione1)
    
        