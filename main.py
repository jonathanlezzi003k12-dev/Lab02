import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("filename.txt")

    txtIn = input()

    # Add input control here!
    #aggiungo le istruzioni di controllo:
    #1 aggiungere una parola
    #2 cercare una traduzione

    if int(txtIn) == 1:
        print()
        txtIn = input()
        pass
    if int(txtIn) == 2:
        pass
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        break
