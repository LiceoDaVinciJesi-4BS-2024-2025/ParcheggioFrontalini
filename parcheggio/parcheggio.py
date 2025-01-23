#Sofia Frontalini
#Classe 4BS
#Esercizio

#1000 auto e 200 moto
#importo la classe PostoMezzo dal file postoMezzo
from postoMezzo import PostoMezzo
from veicolo import Veicolo
#importo datetime e csv
import datetime
import csv
#creo due liste una per la prenotazione del posto e per il csv
listaPrenotazionePosto = []
listaCSV = []
listaAuto = ["FIAT", "FERRARI", "AUDI", "BMW", "MASERATI", "VOLKSWAGEN", "ALFA ROMEO", "MERCEDES"]
#creazione della classe Parcheggio 
class Parcheggio:
    #funzione iniziale con self e nome parcheggio
    def __init__(self, nomeParcheggio):
        #imposto postiLiberiAuto, postiLiberiMoto e guadagnoParcheggio
        self.__nomeParcheggio = nomeParcheggio
        self.__postiLiberiAuto = 1000
        self.__postiLiberiMoto = 200
        self.__guadagnoParcheggio = 0
        
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)
    
    #imposto le property sul nome, postiLiberiAuto, postiLiberiMoto e guadagnoParcheggio per non farlo cambiare da parte dell'utente
    @property
    def nomeParcheggio(self):
        return nomeParcheggio
    
    @property
    def postiLiberiAuto(self):
        return postiLiberiAuto
    
    @property
    def postiLiberiMoto(self):
        return postiLiberiMoto
    
    #funzione di PrenotazionePosto 
    def occupaPosto(self, mezzo: Veicolo):
        #se la tipologia del mezzo è auto
        if mezzo.marca in listaAuto:
            #.. e ci sono ancora posti liberi Auto
            if self.__postiLiberiAuto > 0:
                mezzo.PostoMezzo.occupa(mezzo.targa)
                #tolgo un posto dai postiLiberi
                self.__postiLiberiAuto -= 1
                #calcolo il numeroOreSosta -> data impostata - quella di ora -> calcolo i seconfi e divido per 3600 per trovare le ore
                numeroOreSosta = (mezzo.dataFineParcheggio - mezzo.dataInizioParcheggio).total_seconds() / 3600 
                #calcolo il saldo moltiplicando per 1.5
                saldo = numeroOreSosta * 1.5
                #aggiugno al guadagno del parcheggio il saldo
                self.__guadagnoParcheggio += saldo
                #aggiungo alla lista di prenotazione le caratteristiche del mezzo, numero di ore e saldo 
                listaPrenotazionePosto.append((mezzo.tipologia, mezzo.targa, numeroOreSosta, saldo))
                #aggo
                listaCSV.append({"veicolo": (mezzo.tipologia, mezzo.targa, numeroOreSosta, saldo), "totaleGuadagno" : self.__guadagnoParcheggio})
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
                listaCSV.append({"veicolo": (mezzo.tipologia, mezzo.targa, numeroOreSosta, saldo), "totaleGuadagno" : self.__guadagnoParcheggio})
                return listaPrenotazionePosto
            else:
                return ("I posti sono terminati")
        else:
            raise ValueError("Mezzo non valido")
        
    print(listaCSV)
#     #CREO IL DOCUMENTO PARK.DATA DOVE AGGGIUNGERE I DATI DELLA BIBLIOTECA CHE SI TROVANO NELLA LISTA
#     # importo Path
    from pathlib import Path
#     import csv
    #si crea un nuovo file
    #crea la cartella ovunque essa sia
    nuovoFile = Path.cwd() / "park.data"
    #imposto i campi           
    campi = ["veicolo","totaleGuadagno"]
    #apro il file biblioteca che ho creato
    fileParcheggio = nuovoFile.open("w")
    #imposto lo scrittore       
    scrittore = csv.DictWriter(fileParcheggio, campi)
    #per ogni elemento della listaCSV    
    for riga in listaCSV:
        #lo scrivo nel file
        scrittore.writerow(riga)
    #chiudo il file            
    fileParcheggio.close()
        
#I TEST        
if __name__ == "__main__":
    p = Parcheggio("Il mio Fantastico Parcheggio")
    print(p)
    prenotazione1 = p.occupaPosto(Veicolo("AS 345 WS"))
#     prenotazione2 = p.prenotazionePosto(PostoMezzo("moto", "PK 590 DQ", datetime.datetime(2025, 1, 24, 14, 18, 00)))
#     #prenotazione3 = p.prenotazionePosto(PostoMezzo("camion", "GH 401 QP", datetime.datetime(2025, 1, 22, 20, 18, 00)))
#     prenotazione4 = p.prenotazionePosto(PostoMezzo("auto", "SR 761 KL", datetime.datetime(2025, 1, 25, 17, 18, 00)))
    #prenotazione5 = p.prenotazionePosto(PostoMezzo("moto", "NB 321 BH", datetime.datetime(2025, 1, 19, 20, 18, 00)))
    #print(prenotazione3)
    print(prenotazione1)
    #print(prenotazione5)
    print(p)
        