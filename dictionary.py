class Dictionary:
    def __init__(self):
        self.dizionario=[]

    def loadDictionary(self,language):
        nomeFile=""
        if language == "italian":
            nomeFile="Italian.txt"
        elif language == "english":
            nomeFile="English.txt"
        elif language == "spanish":
            nomeFile="Spanish.txt"
        with open(nomeFile, "r") as file:
            riga=file.readline().strip()
            while riga != "":
                self.dizionario.append(riga)
                riga=file.readline().strip()
            file.close()
        return self.dizionario

    def printAll(self):
        testo=""
        for i in self.dizionario:
            testo+=f"\n{i}"
        print(testo.lstrip("\n"))


    @property
    def dict(self):
        return self._dict