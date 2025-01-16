#Sofia Frontalini
#Classe 4BS
#Classe PostoMezzo

#importo datetime
import datetime

#inserisco tipologia accettabili
tipo = ["auto", "moto"]

#classe PostoMezzo
class PostoMezzo:
    #funzione iniziale
    def __init__(self, tipologia):
        #imposto targa vuota
        self.__targaMezzoParcheggiato = ""
        #controllo con la tipologia inserita sia allì'interno della lista delle tipologie accettabili
        if tipologia.lower() not in tipo:
            raise ValueError("La tipologia non è presente")
        self.__tipologia = tipologia
        #imposto data e ora in cui inserisce la macchina
        self.__datetime = ""
    
    #imposto le property di tipologia, targaMezzoParcheggio, datetime
    @property
    def tipologia(self):
        return tipologia
    
    @property
    def targaMezzoParcheggiato(self):
        return targaMezzoParcheggiato
    
    @property
    def datetime(self):
        return datetime
    
    #imposto le setter
    #controllo che il valore sia all'interno della lista tipo, in caso contrario ritorna errore
    @tipologia.setter
    def tipologia(self, value):
        if value.lower() not in tipo:
            raise ValueError("La tipologia non è presente")
        self.__tipologia = value
    
    #controllo che la targa sia del tipo "AB 123 CD", in caso contrario ritorna errore
    @targaMezzoParcheggiato.setter
    listaTarga = []
    def targaMezzoParcheggiato(self, value) :
        for x in value:
            listaTarga.append(x)
        #per ogni elemento della lista della targa controllo che essa si del tipo "AB 123 CD" tramite le posizioni della lista
        for x in listaTarga:
            if listaTarga[0] in alfabeto and listaTarga[1] in alfabeto and listaTarga[7] in alfabeto and listaTarga[8] in alfabeto and listaTarga[2] == " " and listaTarga[6] == " " and listaTarga[3] in numeri and listaTarga[4] in numeri and listaTarga[5] in numeri:
                self.__targa = value
            else:
                raise ValueError("Targa non valida")
    
    #datetime
    @datetime.setter
    def datetime(self, value):
        self.__datetime = value
        return 
            
    