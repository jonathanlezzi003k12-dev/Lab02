class Translator:


    def __init__(self):
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        print("1) aggiungi una parola")
        # 2. Cerca una traduzione
        print("2) cerca una traduzione ")
        # 3. Cerca con wildcard

        # 4. Exit
        opzione = input ( "seleziona una scelta") #mi salvo in imput la scelta
        return opzione   # la ritorno

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        #devo cercare di salvare ogni riga del file passato come parametro con una struttura dati di tipo chiave valore;
        #quindi devo iterare su ogni riga
        with open("dizonario","r") as dizionario:
            for righe in dizionario:
                riga=righe.split(" ")
                chiave = riga[1].strip()   # seconda parola diventa chiave
                valore = riga[0].strip()   # prima parola diventa valore
                dict[chiave] = valore








    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass
