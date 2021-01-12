from personen_klassen import *

def auslesen():
    f = open('personenliste.txt', 'r')
    while True:
        for i in range(5):
            line = f.readline()
            if not line:
                break
            s = line.split(', ')
            print(s)
            x = Person(s[0], s[1], s[2], s[3], s[4], s[5], s[6], int(s[7]), int(s[8]), int(s[9]), s[10])
            # print(type(x))
    f.close()


print(auslesen())