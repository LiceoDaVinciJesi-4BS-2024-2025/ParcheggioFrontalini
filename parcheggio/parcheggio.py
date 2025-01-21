#Sofia Frontalini
#Classe 4BS
#Esercizio

#1000 auto e 200 moto
from auto import Auto
from moto import Moto
from postoMezzo import PostoMezzo
import datetime
import csv 
listaPrenotazionePosto = []
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
        if mezzo.tipologia == "auto":
            if self.__postiLiberiAuto > 0:
                numeroOreSosta = (mezzo.data - datetime.datetime.now()).total_seconds() / 3600 
                saldo = numeroOreSosta * 1.5
                self.__postiLiberiAuto -= 1
                self.__guadagnoParcheggio += saldo
                listaPrenotazionePosto.append((mezzo.tipologia, mezzo.targa, numeroOreSosta, saldo))
                return listaPrenotazionePosto
            else:
                return ("I posti sono terminati")
        elif mezzo.tipologia == "moto":
            if self.__postiLiberiMoto > 0:
                numeroOreSosta = (mezzo.data - datetime.datetime.now()).total_seconds() / 3600 
                saldo = numeroOreSosta * 1.2
                self.__postiLiberiMoto -= 1
                self.__guadagnoParcheggio += saldo
                listaPrenotazionePosto.append((mezzo.tipologia, mezzo.targa, numeroOreSosta, saldo))
                return listaPrenotazionePosto
            else:
                return ("I posti sono terminati")
        else:
            raise ValueError("Mezzo non valido")
        
    
    #CREO IL DOCUMENTO PARK.DATA DOVE AGGGIUNGERE I DATI DELLA BIBLIOTECA CHE SI TROVANO NELLA LISTA
    # importo Path
    from pathlib import Path
    #creo il percorso desktop
    desktop = Path.home() / "Desktop"
    #creo la cartella ESERCIZI sul desktop
    cartella = desktop / "ParcheggioFrontalini" 
    #si crea un nuovo file 
    nuovoFile = cartella / "park.data"
    #imposto i campi           
    campi = ["veicoli","totaleGuadagno"]
    #apro il file biblioteca che ho creato
    fileParcheggio = nuovoFile.open("w")
    #imposto lo scrittore       
    scrittore = csv.DictWriter(fileParcheggio, campi)
    #per ogni elemento dell lista biblioteca     
    for riga in listaPrenotazionePosto:
        #lo scrivo nel file
        scrittore.writerow(riga)
    #chiudo il file            
    fileParcheggio.close()
        
        
    
if __name__ == "__main__":
    p = Parcheggio("Il mio Fantastico Parcheggio")
    print(p)
    prenotazione1 = p.prenotazionePosto(PostoMezzo("auto", "WE 369 PO", datetime.datetime(2025, 1, 21, 20, 18, 00)))
    prenotazione2 = p.prenotazionePosto(PostoMezzo("moto", "PK 590 DQ", datetime.datetime(2025, 1, 22, 14, 18, 00)))
    #prenotazione3 = p.prenotazionePosto(PostoMezzo("camion", "GH 401 QP", datetime.datetime(2025, 1, 22, 20, 18, 00)))
    prenotazione4 = p.prenotazionePosto(PostoMezzo("auto", "SR 761 KL", datetime.datetime(2025, 1, 25, 17, 18, 00)))
    #prenotazione5 = p.prenotazionePosto(PostoMezzo("moto", "NB 321 BH", datetime.datetime(2025, 1, 19, 20, 18, 00)))
    #print(prenotazione3)
    print(prenotazione4)
    #print(prenotazione5)
        