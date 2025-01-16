#Sofia Frontalini
#Classe 4BS
#Classe PostoMezzo

import datetime 
tipo = ["auto", "moto"]
class PostoMezzo:
    def __init__(self, tipologia):
    self.__targaMezzoParcheggiato = ""
        if tipologia.lower() not in tipo:
            raise ValueError("La tipologia non è presente")
        self.__tipologia = tipologia
            