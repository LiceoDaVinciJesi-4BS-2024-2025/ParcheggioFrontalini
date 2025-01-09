#Sofia Frontalini
#Classe 4BS
#Classe Veicolo

listaMarca = ["FIAT", "FERRARI", "AUDI", "BMW", "MASERATI", "VOLKSWAGEN", "ALFA ROMEO", "MERCEDES", "FANTIC", "BETA", "E-SCOOTER", "SUZUKI", "PEUGEOT", "HARLEY-DAVIDSON"]
listaColore = ["nero", "bianco", "rosso", "blu", "verde", " fucsia", "arancione", "gialla", "viola", "grigio"]
listaAlimentazione = ["Diesel", "Ibrido", "Elettrico", "Benzina"]
alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
class Veicolo:
    def __init__(self, targa):
        self.__marca = "Fiat"
        self.__modello = "Panda"
        self.__colore = "Fucsia"
        self.__cilindrata = 1000
        self.__alimentazione = "Diesel"
        listaTarga = []
        for x in targa:
            listaTarga.append(x)
            if 
        self.__targa = targa.upper()
        
    #funzione necessaria per visualizzare la classe
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
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
    
    @marca.setter
    def marca(self, value):
        if value not in listaMarca:
            raise ValueError ("La marca non è presente")
        
        self.__marca = value
        return 
    
    @modello.setter
    def modello(self, value):
        self.__modello = value
        return
    
    @colore.setter
    def colore(self, value):
        if value not in listaColore:
            raise ValueError ("Il colore non è presente")
        
        self.__colore = value
        return
    
    @alimentazione.setter
    def alimentazione(self, value):
        if value not in listaAlimentazione:
            raise ValueError ("L'alimentazione non è presente")
        
        self.__alimentazione = value
        return 
        
    @cilindrata.setter
    def cilindrata(self, value):
        if value // 100 != 0 or type(value) != int or value < 0:
            raise ValueError ("La cilindrata non è un intero positivo multiplo di 100.")
        
        self.__cilindrata = value
        return 
        
        
