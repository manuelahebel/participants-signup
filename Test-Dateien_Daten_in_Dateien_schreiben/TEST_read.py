import personen_klassen as pk

f = open('personenliste.txt', 'r')

while True:
    for i in range(5):
        line = f.readline()
        if not line:
            break
        s = line.split(', ')
        print(s)
        #print(type(s))
        x = pk.Person(s[0], s[1], s[2], s[3], s[4], s[5], s[6], int(s[7]), int(s[8]), int(s[9]), s[10])
        print(type(x))
f.close()




# f_string = f.read()
# print(f_string)
# f_string_splitted = f_string.split(', ')
#
# print(f_string_splitted[10])
#
# f.close()


# x = 'Hallo, Welt, schön, ist, es, hier.'
#
# y = x.split(', ')
# print(y)
#
# #y = y.strip()
#
# print(y[2])

