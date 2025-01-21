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
    def __init__(self, tipologia):
    
        #controllo con la tipologia inserita sia allì'interno della lista delle tipologie accettabili
        if tipologia.lower() not in tipo:
            raise ValueError("La tipologia non è presente")
        self.__tipologia = tipologia
        
        #imposto targa vuota
        self.__targa = ""
        
        #imposto data e ora in cui inserisce la macchina
        self.__data = ""
    
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    #imposto le property di tipologia, targaMezzoParcheggio, datetime
    @property
    def tipologia(self):
        return tipologia
    
    @property
    def targa(self):
        return targa
    
    @property
    def data(self):
        return data
    
    #imposto le setter
    #controllo che il valore sia all'interno della lista tipo, in caso contrario ritorna errore
    @tipologia.setter
    def tipologia(self, value):
        if value.lower() not in tipo:
            raise ValueError("La tipologia non è presente")
        self.__tipologia = value
    
    
    #controllo che la targa sia del tipo "AB 123 CD", in caso contrario ritorna errore
    @targa.setter
    def targa(self, value):
        listaTarga = []
        for x in value:
            listaTarga.append(x)
        #per ogni elemento della lista della targa controllo che essa si del tipo "AB 123 CD" tramite le posizioni della lista
        for x in listaTarga:
            if listaTarga[0] in alfabeto and listaTarga[1] in alfabeto and listaTarga[7] in alfabeto and listaTarga[8] in alfabeto and listaTarga[2] == " " and listaTarga[6] == " " and listaTarga[3] in numeri and listaTarga[4] in numeri and listaTarga[5] in numeri:
                self.__targa = value
            else:
                raise ValueError("Targa non valida")
    
    #datetime
    @data.setter
    def data(self, value):
        if type(value) != datetime.datetime or value > datetime.datetime.now():
            raise ValueError("Data/Ora non valida")
        self.__data = value
        return 
            
if __name__ == "__main__":
    p1 = PostoMezzo("auto")
    print(p1)
    p1.targa = "AB 347 DF"
    p1.data = datetime.datetime(2025, 1, 20, 20, 18, 00)
    print(p1)