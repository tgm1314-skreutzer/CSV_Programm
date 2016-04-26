import csv

class csvVerbindung:
    """
    Diese Klasse liest ein csv-File ein

    """
    def __init__(self, file):
        """
        Konstruktor
        :param file: das zulesende File
        :return:None
        """
        self.file = file #setzt das File
        self.lines = []
        self.header = []

    def einlesen(self):
        """
        liest ein gewuenschtes csv-File und speichert dies in Daten
        :return: Inhalt des Files
        """
        with open(self.file, 'r') as csvfile: #oeffnet des gewuenschte File
            try:
                dialect = csv.Sniffer().sniff(csvfile.read(), ['\t', ';', ',', ' ', ':', '|'])
            except:
                dialect = None

            csvfile.seek(0)#dadurch geht er jedes Element durch
            #daten=''
            #daten = [] Daten in der Methode selbst zu definieren wurde verworfen, da schreiben ebenfalls auf diese Daten zugreifen muss
            freader = csv.reader(csvfile, dialect, quotechar='|')
            self.header = next(freader)
            for line in freader:
                self.lines.append(line)
            print('reader:')
            print(self.header)
            print('_____________')
            print(self.lines)
            return self.lines, self.header


            #for row in freader: Die Version mit der Schleife wurde ebenfalls verworfen
                #print(', '.join(row)) liest ein csv File mit dem Dialekt ; ein
                #daten=daten.join(row) schreibt die ausgelesenen Daten in einer Schlange zusammen.
                #daten=daten.join(', '.join(row)) erste Varainte war mit String. Beim Ueberlegen hat sich dies jedoch problematisch erwiesen, weil man beim schreiben dies wierder extra auslesen muss,wenn man das gelesene nochmals schreiben will
                #self.daten.append(row)

            #self.daten=list(freader)
            #print(self.daten)
            #return self.daten


    def schreiben(self):
        """
        schreibt ein csv-File
        :return:
        """
        with open(self.file, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',quotechar='|',quoting=csv.QUOTE_NONE)
            daten=[]
            daten.append(self.header)
            for line in self.lines:
                daten.append(line)
            print('writer:')
            print(daten)
            writer.writerows(daten)




if __name__ == '__main__':
    csvV = csvVerbindung('/home/sarahkreutzer/Desktop/csv_test.csv')
    csvV.einlesen()
    csvV.schreiben()


