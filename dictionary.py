class Dictionary:
    def __init__(self):
        pass

    def addWord(self,parola_aliena,parola_umana):
        with open("dizionario","a") as dizionario:
            dizionario.add(str(parola_aliena)+" "+str(parola_umana))


    def translate(self):

        pass

    def translateWordWildCard(self):
        pass
