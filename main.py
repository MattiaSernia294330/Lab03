import spellchecker
import time

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()


    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        start = time.time()
        sc.handleSentence(txtIn,"italian")
        end = time.time()
        timePassed=end-start
        print(f"time elapsed: {timePassed}")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        start = time.time()
        sc.handleSentence(txtIn,"english")
        end = time.time()
        print(f"time elapsed: {timePassed}")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        start = time.time()
        sc.handleSentence(txtIn,"spanish")
        end = time.time()
        print(f"time elapsed: {timePassed}")
        continue

    if int(txtIn) == 4:
        break


