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
        #controllo che il tipoVeicolo sia all'interno della lista
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
    
    #imposto la proprietà su tipoVeicolo, targa, dataInizioParcheggio e dataFineParcheggio
    @property
    def tipoVeicolo(self):
        return self.__tipoVeicolo
    
    @property
    def targa(self):
        return self.__targa
    
    @property
    def dataInizioParcheggio(self):
        return self.__dataInizioParcheggio
    
    @property
    def dataFineParcheggio(self):
        return self.__dataFineParcheggio
    
#     @targa.setter
#     def targa(self, value):
#         listaTarga = []
#         #per ogni elemento dellaa targa lo aggiungo alla lista
#         for x in value:
#             listaTarga.append(x)
#         #per ogni elemento della lista della targa controllo che essa si del tipo "AB 123 CD" tramite le posizioni della lista
#         for x in listaTarga:
#             if listaTarga[0] in alfabeto and listaTarga[1] in alfabeto and listaTarga[7] in alfabeto and listaTarga[8] in alfabeto and listaTarga[2] == " " and listaTarga[6] == " " and listaTarga[3] in numeri and listaTarga[4] in numeri and listaTarga[5] in numeri:
#                 self.__targa = value.upper()
#             else:
#                 raise ValueError("Targa non valida")
#     
    #imposto le setter su dataInizioParcheggio e dataFineParheggio
    @dataInizioParcheggio.setter
    def dataInizioParcheggio(self, value):
        if value != datetime.datetime.now():
            raise ValueError("Data non valida")
        self.__dataInizioParcheggio == value   
        
    @dataFineParcheggio.setter
    def dataFineParcheggio(self, value):
        if value != datetime.datetime.now():
            raise ValueError("Data non valida")
        self.__dataFineParcheggio == value   
    
    #funzione occupaPosto
    def occupaPosto(self, targa):
        #la targa diventa quella inserita
        self.__targa = targa
        #e la dataInzioParcheggio quella di quel momento
        self.__dataInizioParcheggio = datetime.datetime.now()
        return
    
    #funzione liberaPosto
    def liberaPosto(self, targa):
        #se la targa è uguale
        if targa == self.__targa:
            #il self targa diventa vuto
            self.__targa = ""
            #e la dataFineParcheggio quella di quel momento
            self.__dataFineParcheggio = datetime.datetime.now()
        return
    
    #funzione occupato
    def occupato(self):
        #se la targa è vuota
        if self.__targa == "":
            #tiortna falso
            return False
        #ritorna vero
        return True

#I TEST
if __name__ == "__main__":
    p1 = PostoMezzo("auto")
    print(p1)
    p1.targa = "AB 347 DF"
    print(p1)
    p1.occupaPosto("AB 347 DF")
    print(p1)
    p1.liberaPosto("AB 347 DF")
    print(p1)
