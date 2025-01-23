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
    def __init__(self, tipologia, targa):
    
        #controllo con la tipologia inserita sia allì'interno della lista delle tipologie accettabili
        if tipologia.lower() not in tipo:
            raise ValueError("La tipologia non è presente")
        self.__tipologia = tipologia
        
        #imposto targa vuota
        self.__targa = " "
        
        #imposto data e ora in cui inserisce la macchina

        self.__dataInizioParcheggio = None
        self.__dataFineParcheggio = None
    
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    #imposto le property di tipologia, targaMezzoParcheggio, datetime
    @property
    def tipologia(self):
        return self.__tipologia
    
    @property
    def targa(self):
        return self.__targa
    
    @property
    def data(self):
        return self.__data
    
    #imposto le setter
    #controllo che il valore sia all'interno della lista tipo, in caso contrario ritorna errore
    @tipologia.setter
    def tipologia(self, value):
        if value.lower() not in tipo:
            raise ValueError("La tipologia non è presente")
        self.__tipologia = value
    
    #datetime
    @data.setter
    def data(self, value):
        if type(value) != datetime.datetime or value < datetime.datetime.now():
            raise ValueError("Data/Ora non valida")
        self.__data = value
        return
    
    def occupaPosto(self, targa):
        self.__targa = targa
        self.__dataInizioParcheggio = datetime.datetime.now()
        return
    
    def liberaPosto(self, targa, data):
        self.__targa = targa
        self.__dataFineParcheggio = datetime.datetime.now()
        return
    
    def occupato(self):
        if self.__targa == "":
            return False
        return True
             
if __name__ == "__main__":
    p1 = PostoMezzo("auto", " ", "None")
    print(p1)
    p1.targa = "AB 347 DF"
    p1.data = datetime.datetime(2025, 1, 20, 20, 18, 00)
    print(p1)