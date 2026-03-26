class Translator:


    def __init__(self):
        self.dizz= {}

    def printMenu(self):
        # 1. Aggiungi nuova parola
        print("1) aggiungi una parola")
        # 2. Cerca una traduzione
        print("2) cerca una traduzione ")
        # 3. Cerca con wildcard
        print("3) cerca con wildcard")
        # 4. Exit
        print ("4) esci")


    def loadDictionary(self):
        # dict is a string with the filename of the dictionary
        #devo cercare di salvare ogni riga del file passato come parametro
        # con una struttura dati di tipo chiave valore;
        #quindi devo iterare su ogni riga
        with open("dictionary.txt","r") as dizionario:
            for righe in dizionario:
                riga=righe.split(" ")
                chiave = riga[0].strip()   # seconda parola diventa chiave
                valore = riga[1].strip()   # prima parola diventa valore
                self.dizz[chiave] = valore      #quindi la chiave è la parola aliena mentre il valore è la parola in italiano


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        #questi metodi gestiscono gli imput;
        #nel senso che vedono se l'utente ha fatto  degli errori in imput
        #poi chiamano la funzione incaricata a svolgere quel compito e gli passano i dati
        #in questo caso ho handleadd quindi gestisco le aggiunte nel dizionario



        parole=entry.split()
        parola_aliena=parole[0]
        parola_italiana=parole[1]
        #controllo sulla lunghezza della parola inoltre la rendo minuscola
        if(len(parola_aliena)<2):
           print("non esiste nessuna parola aliena così corta; errore")
           return
        if (len(parola_italiana)<2):
            print("non esiste nessuna parola aliena così corta; errore")
            return
        risultato:str=(parola_aliena.lower()+" "+parola_italiana.lower())
        return risultato






    def handleTranslate(self, query:str):
        # query is a string <parola_aliena>
        #qui devo cercare la traduzione di una parola esistente inserendo
        # la parola aliena e inserendo la tarduzione la
        #parola tradotta comparirà sul terminale

        #>==============================================================================================================
        #1) mi salvo la parola da tradurre in una variabile
        #2) controllo se esiste un vaole all'interno del dizionario che ha come chiave la parola salvata
        #3) controllo lunghezza
        #4) restituisco la parola


        parola_da_cercare:str=query.strip().lower()
        if len(parola_da_cercare)<2:
            print("la parola non esiste perchè troppo corta")
            return
        elif(parola_da_cercare in self.dizz):
            return parola_da_cercare
        else:
            print("la parola non è presente all'interno del dizionario")
            return




    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass
