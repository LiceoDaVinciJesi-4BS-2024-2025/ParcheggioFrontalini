#Sofia Frontalini
#Classe 4BS
#Classe Veicolo

#creazione delle liste che mi servono per la classe veicolo -> Marca, Colore, Alimentazione
listaMarca = ["FIAT", "FERRARI", "AUDI", "BMW", "MASERATI", "VOLKSWAGEN", "ALFA ROMEO", "MERCEDES", "FANTIC", "BETA", "E-SCOOTER", "SUZUKI", "PEUGEOT", "HARLEY-DAVIDSON"]
listaColore = ["nero", "bianco", "rosso", "blu", "verde", " fucsia", "arancione", "gialla", "viola", "grigio"]
listaAlimentazione = ["diesel", "ibrido", "elettrico", "benzina"]
listaVeicoli = []

#creazione della stringa alfabeto e numeri
alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
numeri = "1234567890"

#Classe Veicolo
class Veicolo:
    #funzione iniziale con parametri self e targa
    def __init__(self, targa):
        #impostazione della marca, modello, colore, cilindraata, alimentazione a mia scelta
        self.__marca = "FIAT"
        self.__modello = "Panda"
        self.__colore = "fucsia"
        self.__cilindrata = 1000
        self.__alimentazione = "diesel"
        #creazione della lista targa 
        listaTarga = []
        #per ogni elemento dellaa targa lo aggiungo alla lista
        for x in targa:
            listaTarga.append(x)
        #per ogni elemento della lista della targa controllo che essa si del tipo "AB 123 CD" tramite le posizioni della lista
        for x in listaTarga:
            if listaTarga[0] in alfabeto and listaTarga[1] in alfabeto and listaTarga[7] in alfabeto and listaTarga[8] in alfabeto and listaTarga[2] == " " and listaTarga[6] == " " and listaTarga[3] in numeri and listaTarga[4] in numeri and listaTarga[5] in numeri:
                self.__targa = targa.upper()
            else:
                raise ValueError("Targa non valida")
#         
#         veicolo = (self.__marca, self.__modello, self.__cilindrata)
#         listaVeicoli.append(veicolo)
        
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    #imposto le proprietà su marca, modello, colore, cilindrata, alimentazione, targa
    @property
    def marca(self):
        return marca
    
    @property
    def modello(self):
        return modello
    
    @property
    def colore(self):
        return colore
    
    @property
    def cilindrata(self):
        return cilindrata
    
    @property
    def alimentazione(self):
        return alimentazione
    
    @property
    def targa(self):
        return targa
    
    #imposto le setter
    
    #è possibile camabiare la marca solamente se è all'interno della lista sennò ritorna errore
    @marca.setter
    def marca(self, value):
        if value.upper() not in listaMarca:
            raise ValueError ("La marca non è presente")
        
        self.__marca = value.upper()
        return 
    
    
    #è possibile camabiare il modello
    @modello.setter
    def modello(self, value):
        self.__modello = value
        return
    
    #è possibile cambiare il colore solamente se è all'interno della lista sennò ritorna errore
    @colore.setter
    def colore(self, value):
        if value.lower() not in listaColore:
            raise ValueError ("Il colore non è presente")
        
        self.__colore = value.lower()
        return
    
    #è possibile cambiare l'alimentazione solamente se è all'interno della lista sennò ritorna errore
    @alimentazione.setter
    def alimentazione(self, value):
        if value not in listaAlimentazione:
            raise ValueError ("L'alimentazione non è presente")
        
        self.__alimentazione = value
        return
    
    #è possibile camabiare la cilindrata solamente se è un intero positivo multiplo di 100  
    @cilindrata.setter
    def cilindrata(self, value):
        if value % 100 != 0 or type(value) != int or value < 0:
            raise ValueError ("La cilindrata non è un intero positivo multiplo di 100.")
        
        self.__cilindrata = value

        return
    
#     def __lt__(self, other):
#         if self.__marca == other.__marca:
#             if self.__modello == other.__modello:
#                 return self.__cilindrata < other.__cilindrata
#             return self.__modello < other.__modello
#         return self.__marca < other.__marca
#     
#     def __repr__(self):
#         return f"Veicolo(marca={self.marca}, modello={self.modello}, targa={self.targa})"
#
#Faccio i test
if "__main__" == __name__:
    v1 = Veicolo("AD 123 SE")
    v2 = Veicolo("AS 345 WS")
    v2.marca = "Ferrari"
    v2.cilindrata = 1500
    print(v2)
    print(v1)

