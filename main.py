import translator as tr
import dictionary as dz

 #quindi inizializza il  costruttore di traslator  traslator con un dizionario vuoto
t = tr.Translator()
d=dz.Dictionary()

while(True):
    #chiama il metodo menù appartenente a Traslator che si trova all'interno di traslator
    #questo mi fa vedere a schermo le opzioni del menù
    t.printMenu()
    #questo serve a caricare il dizionario voto con uno esistente presente in un formato txt
    t.loadDictionary()
    #l'imput
    txtIn:int = input("inserisci il numero per iniziare ad operare")

    # Add input control here!
    #aggiungo le istruzioni di controllo:
    #1 aggiungere una parola
    #2 cercare una traduzione



    #se il numero è uno devo aggiungere una parola
    #per aggiungere una parola devo chiamare il metodo addword all'interno di dictionary che a sua volta
    #per effettuare i controlli chiama il metodo hendleaddworld di translator
    if int(txtIn) == 1:

        print("hai selezionato l'ozione di aggiungere la parola ")

        parola_grezza_da_aggiungere:str = input("inserisci le parole da aggiungere al dizionario seguendo l'ordine:"
                      " parola aliena parola tradotta in italiano")
        #d è un oggetto di tipo dizionario che ci permette di utilizzare la classe presente in dictionary per
        #aggiungere una parola
        d.addWord(parola_grezza_da_aggiungere)

    if int(txtIn) == 2:
        pass
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        break

