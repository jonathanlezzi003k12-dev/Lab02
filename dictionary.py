from translator import Translator


class Dictionary:

    def __init__(self):
        #il dio dizionario lo inizializzo caricando il mio dizionari attraverso l'inizializzazione di translator
        #e attraverso l'utilizzo del metodo loadDictionary
        self.dizionario_corrente=Translator().loadDictionary()






    #questo metodo mi serve per aggiungere la parola più la traduzione;
    #per farlo devo :
    # -aprire il mio dizionario in modalità append
    # -passare al metodo hendleadd la query e poi recuperare il return
    # -inserire in fine il return nel dizionario

    def addWord(self,aggiungo_parola):

        #mi faccio dire la traduzione i output
        ##aggiungo_parola=input("inserisci le parole da aggiungere al dizionario seguendo l'ordine: parola aliena"
                            ## "  parola tradotta in italiano")
        #passo il testo della traduzione come parametro della funzione di controllo handle per ottenere come risultato
        #la stringa da aggiungere


        #oggetto di tipo traslator
        t= Translator()
        risultato=t.handleAdd(aggiungo_parola)
        #piccola verifica per gestire il none dato dal return dell metodo hendleadd di traslator
        if (risultato is not None):
            stringa_da_aggiungere_al_dizionario:str=risultato
            with open("dictionary.txt","a") as dizionario:
                dizionario.write(stringa_da_aggiungere_al_dizionario)
                print(stringa_da_aggiungere_al_dizionario)
        else:
            return








    def translate(self):
        #step per risolvere il metodo; io voglio che questo metodo mi chiami
        # il metodo heandle in traslate per verificare la stringa in ingresso
        #e in base a quello che mi ritorna cercare o meno la parola all'interno del dizionario


        #1) input; prendere in input una parola
        #2) chiamare la funzione handle
        #3) valutarne il return e se la parola era preente all'interno del dizz restituire la traduzione
        #4) se invece la parola non è presente farlo sapere all'utente


        parola_da_tradurre:str=input("inserisci una parola aliena per la quale vuoi vedere la traduzione in italiano ")
        output_metodo_hendletraslate=self.dizz.handleTranslate(parola_da_tradurre)
        if(output_metodo_hendletraslate is not  None):
            return self.dizz[output_metodo_hendletraslate]







    def translateWordWildCard(self):
        pass
