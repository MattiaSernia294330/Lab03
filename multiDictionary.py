import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.lista=[]

    def printDic(self, language):
        diz=d.Dictionary()
        diz.loadDictionary(language)
        diz.printAll()


    def searchWord(self, words, language):
        dizionario=d.Dictionary()
        dizionario=dizionario.loadDictionary(language)
        testo = words.split(" ")
        self.lista.clear()
        for i in testo:
            j=rw.RichWord(i)
            if i not in dizionario:
                j.__setattr__('corretta', False)
                self.lista.append(j)
        return self.lista
    def searchWordlinear(self, words, language):
        dizionario=d.Dictionary()
        dizionario=dizionario.loadDictionary(language)
        testo = words.split(" ")
        self.lista.clear()
        for i in testo:
            j=rw.RichWord(i)
            for e in dizionario:
                if e==i:
                    break
            j.__setattr__('corretta', False)
            self.lista.append(j)
        return self.lista


