import time
import dictionary

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass


    def handleSentence(self, txtIn, language):
        errori=""
        txtIn=replaceChars(txtIn)
        txtIn=txtIn.lower()
        l=md.MultiDictionary()
        lista=l.searchWord(txtIn,language)
        for e in lista:
            if e.corretta==False:
                errori+=f"\n{e}"
        print (errori.lstrip("\n"))




    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~?"
    for c in chars:
        text = text.replace(c, "")
    return text