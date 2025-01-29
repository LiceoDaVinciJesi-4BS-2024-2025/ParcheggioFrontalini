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
        self.__tipoVeicolo = tipoVeicolo
            
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
    
    @targa.setter
    def targa(self, value):
        listaTarga = []
        #per ogni elemento dellaa targa lo aggiungo alla lista
        for x in value:
            listaTarga.append(x)
        #per ogni elemento della lista della targa controllo che essa si del tipo "AB 123 CD" tramite le posizioni della lista
        for x in listaTarga:
            if listaTarga[0] in alfabeto and listaTarga[1] in alfabeto and listaTarga[7] in alfabeto and listaTarga[8] in alfabeto and listaTarga[2] == " " and listaTarga[6] == " " and listaTarga[3] in numeri and listaTarga[4] in numeri and listaTarga[5] in numeri:
                self.__targa = value.upper()
            else:
                raise ValueError("Targa non valida")
            
    @dataInizioParcheggio.setter
    def dataInizioParcheggio(self, value):
        if value != datetime.datetime.now() or value != None:
            raise ValueError("Data non valida")
        elif value == datetime.datetime.now():
            self.__dataInizioParcheggio == datetime.datetime.now()
        self.__dataInizioParcheggio == None 
        
        
    @dataFineParcheggio.setter
    def dataFineParcheggio(self, value):
        if value != datetime.datetime.now() or value != None:
            raise ValueError("Data non valida")
        elif value == datetime.datetime.now():
            self.__dataFineParcheggio == datetime.datetime.now()
        self.__dataFineParcheggio == None 
        
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
    p1 = PostoMezzo("auto")
    print(p1)
    p1.targa = "AB 347 DF"
    p1.dataInizioParcheggio = datetime.datetime.now()
    print(p1)
    p1.occupaPosto("AB 347 DF")
