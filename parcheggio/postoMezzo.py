#Sofia Frontalini
#Classe 4BS
#Classe PostoMezzo

#importo datetime
import datetime
#creazione della stringa alfabeto e numeri
alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
numeri = "1234567890"

#inserisco tipologia accettabili
tipo = ["auto", "moto"]

#classe PostoMezzo
class PostoMezzo:
    #funzione iniziale
    def __init__(self, tipoVeicolo):
        
        if tipoVeicolo not in tipo:
            raise ValueError("il tipo di veicolo non è accettabile")
        self:__tipoVeicolo = tipoVeicolo
            
        #imposto targa vuota
        self.__targa = "" 
        
        #imposto data e ora in cui inserisce la macchina

        self.__dataInizioParcheggio = None
        self.__dataFineParcheggio = None
    
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
         return self.__class__.__name__ + str(self.__dict__)
    
    
    @property
    def targa(self):
        return self.__targa
    
    @property
    def dataInizioParcheggio(self):
        return self.__dataInizioParcheggio
    
    @property
    def dataFineParcheggio(self):
        return self.__dataFineParcheggio
    
    def occupaPosto(self, targa):
        self.__targa = targa
        self.__dataInizioParcheggio = datetime.datetime.now()
        return
    
    def liberaPosto(self, targa):
        if targa == self.__targa:
            self.__targa = "" 
            self.__dataFineParcheggio = datetime.datetime.now()
        return
    
    def occupato(self):
        if self.__targa == "":
            return False
        return True
             
if __name__ == "__main__":
    # PROF: guarda la init ---> PostoMezzo NON prende parametri. Ma è giusto?? Almeno il tipo... ci vuole, no??
    p1 = PostoMezzo("auto")
    print(p1)
    p1.targa = "AB 347 DF"
    p1.dataInizioParcheggio = datetime.datetime(2025, 1, 20, 20, 18, 00)
    print(p1)