#Sofia Frontalini
#Classe 4BS
#Esercizio

#importo tutte le classi create dai rispettivi file
from postoMezzo import PostoMezzo
from veicolo import Veicolo
from auto import Auto
from moto import Moto
#importo datetime, pathlib e csv
import datetime
from pathlib import Path
import csv

#classe Parcheggio
class Parcheggio:
    #funzione inziale
    def __init__(self, nomeParcheggio):
        self.__nomeParcheggio = nomeParcheggio
        #imposto la creazione di liste per i posti auto(1000) e moto(200)
        self.__postiAuto=[]
        for n in range(1000):
            posto = PostoMezzo("auto")
            self.__postiAuto.append(posto)
            
        self.__postiMoto = []
        for n in range(200):
            posto = PostoMezzo("moto")
            self.__postiMoto.append(posto)
        
        #imposto il guadagno del parcheggio uguale a 0
        self.__guadagno = 0
        
        #if Path("park.data").exists():
            #self.lettura()
            
            
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__) 
    
    #imposto le proprietà
    @property
    def nomeParcheggio(self):
        return self.__nomeParcheggio
    
    @property
    def postiAuto(self):
        return self.__postiAuto
    
    @property
    def postiMoto(self):
        return self.__postiMoto
    
    @property
    def guadagno(self):
        return self.__guadagno
    
    #funzione parcheggio prende come attributo un veicolo
    def parcheggia(self, veicolo: Veicolo):
        #se il tipo è un auto
        if isinstance(veicolo, Auto):
            #controllo che i posti della lista non siano tutti occupati e ne occupo uno
            for posto in self.__postiAuto:
                if not posto.occupato():
                    posto.occupaPosto(veicolo.targa)
                    #ritorna vero
                    return True
                
            #posti auto pieni
            return False
        
        #UGUALE PER LE MOTO
        if isinstance(veicolo, Moto):
            for posto in self.__postiMoto:
                if not posto.occupato():
                    posto.occupaPosto(veicolo.targa)
                    return True
            
            return False
    
    #funzione libera sempre con attributo veicolo
    def libera(self, veicolo: Veicolo):
        #se il tipo è un auto
        if isinstance(veicolo, Auto):
            #trovo il veicolo all'interno della lista
            for posto in self.__postiAuto:
                #uso la funzione di postoMezzo per liberare il posto
                posto.liberaPosto(veicolo.targa)
                #calcolo il numero di ore
                numeroOre = (datetime.datetime.now() - posto.dataInizioParcheggio).total_seconds() / 3600
                #calcolo il saldo moltiplicandolo *1.5 e lo aggiungo al guadagno del parcheggio
                saldo = numeroOre * 1.5
                self.__guadagno += saldo
                #ritorna vero
                return saldo
            #ritorna falso
            return "Non è possibile liberare il posto perchè macchina non presente"
        
        #UGUALE PER LE MOTO
        if isinstance(veicolo, Moto):
            for posto in self.__postiMoto:
                posto.liberaPosto(veicolo.targa)
                numeroOre = (datetime.datetime.now() - posto.dataInizioParcheggio).total_seconds() / 3600
                saldo = numeroOre * 1.2
                self.__guadagno += saldo
                #ritorna vero
                return saldo
            #ritorna falso
            return "Non è possibile liberare il posto perchè moto non presente"
        
    #funzione di scrittura
    def scrittura(self):
        #creo la lista per i dati da Inserire
        datiDaInserire = []
        #insierisco nella lista il tipoveicolo, targa, dataInzioParcheggio e dataFineParcheggio sia della lista dei postiAuto sia della lista dei postiMoto
        for posto in self.__postiAuto:
            #if posto.dataInizioParcheggio == None and posto.dataFineParcheggio == None:
            if posto.targa == "":
                datiDaInserire.append({"tipoVeicolo": "auto", "targa":posto.targa,"dataInizioParcheggio": "data non presente", "dataFineParcheggio":"data non presente"})
            elif posto.targa != "" and posto.dataInizioParcheggio != None:
                datiDaInserire.append({"tipoVeicolo": "auto", "targa":posto.targa,"dataInizioParcheggio": datetime.datetime.strftime(posto.dataInizioParcheggio, "%Y-%m-%d %H:%M:%S"), "dataFineParcheggio": "data non presente"})
            else:
                datiDaInserire.append({"tipoVeicolo": "auto", "targa":posto.targa,"dataInizioParcheggio": posto.dataInizioParcheggio, "dataFineParcheggio": posto.dataFineParcheggio})
            
        for posto in self.__postiMoto:
            if posto.targa == "":
                datiDaInserire.append({"tipoVeicolo": "moto", "targa":posto.targa,"dataInizioParcheggio": "data non presente", "dataFineParcheggio":"data non presente"})
            elif posto.targa != "" and posto.dataInizioParcheggio != None:
                datiDaInserire.append({"tipoVeicolo": "moto", "targa":posto.targa,"dataInizioParcheggio": datetime.datetime.strftime(posto.dataInizioParcheggio, "%Y-%m-%d %H:%M:%S"), "dataFineParcheggio":posto.dataFineParcheggio})
            else:
                datiDaInserire.append({"tipoVeicolo": "moto", "targa":posto.targa,"dataInizioParcheggio": posto.dataInizioParcheggio, "dataFineParcheggio": posto.dataFineParcheggio})

                
        #creo il nuovo file dive su trova tutta la cartella e lo apro
        nuovoFile = Path.cwd() / "park.data"
        fileParcheggio = nuovoFile.open("w")
        
        #come capi prendo quelli che si trovano nella lista
        campi = ["tipoVeicolo", "targa", "dataInizioParcheggio", "dataFineParcheggio"]
        
        #attivo lo scrittore
        scrittore = csv.DictWriter(fileParcheggio, campi)
        scrittore.writeheader()
    
        #per ogni riga nei datiDaInserire
        for riga in datiDaInserire:
            #lo faccio srivere sul file
            scrittore.writerow(riga)
        
        #scrivo sul file anche il totale del guadagno
        fileParcheggio.write(str(self.__guadagno))
        
        #chiudo il file
        fileParcheggio.close()
        return
    
#     def lettura(self):
#         # la lista su cui caricheremo i dati
#         datiAuto = []
#         datiMoto = []
# 
#         file = open("park.data", "r")
#         lettore = csv.DictReader(file)
# 
#         for riga in lettore:
#             if riga["tipoVeicolo"] == "auto" or riga["tipoVeicolo"] == "moto":
#                 if riga["dataInizioParcheggio"] == "data non presente" or riga["dataFineParcheggio"] == "data non presente":
#                     parcheggioAuto = PostoMezzo(riga["tipoVeicolo"], riga["targa"], None, None)                    
#                 elif riga["dataInizioParcheggio"] != None:
#                     parcheggioAuto = PostoMezzo(riga["tipoVeicolo"], riga["targa"], datetime.datetime.strptime(riga["dataInizioParcheggio"], "%Y-%m-%d %H:%M:%S")) 
#                     datiAuto.append(parcheggioAuto)
#                 else:
#                     parcheggioAuto = PostoMezzo(riga["tipoVeicolo"], riga["targa"], datetime.datetime.strptime(riga["dataInizioParcheggio"], "%Y-%m-%d %H:%M:%S"), datetime.datetime.strptime(riga["dataFineParcheggio"], "%Y-%m-%d %H:%M:%S"))
#                     datiAuto.append(parcheggioAuto)
#                     
#             else:
#                 self.__guadagno = float(riga["tipoVeicolo"])
#         
#          #ricreo le liste del parcheggio
#         self.__postiAuto= datiAuto
#         self.__postiMoto= datiMoto
#         file.close()
#         return 
            
#FACCIO I TEST                
if __name__ == "__main__":
    p = Parcheggio("ParcheggioFrontalini")
    print(p)
    auto1 = p.parcheggia(Auto("AS 134 DE", 5, 2, 600))
    print(auto1)
    moto1 = p.parcheggia(Moto("TR 892 OI", 2, 1, 100))
    print(moto1)
    print(p)
    auto2 = p.parcheggia(Auto("QW 457 DP", 7, 4, 1000))
    print(auto2)
    print(p)
    print(p.scrittura())
    print(p.lettura())
    
    #dopo un po'
#     auto1Libera = p.libera(Auto("AS 234 DE", 5, 3, 1000))
#     print(auto1Libera)
#     moto1Libera = p.libera(Moto("TR 892 OI", 2, 1, 100))
#     print(moto1Libera)
    print(p)
    print(p.scrittura())
    
