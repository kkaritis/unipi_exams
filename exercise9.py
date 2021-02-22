# THE USER GIVE AN ASCII FILE AND EACH LETTER WILL BE PUTTED IN THE LIST IN QUEUE

arxeio = input("give an ASCII file ")
list_char1 = []
l = len(arxeio)
for i in range(0,l):
    letter = arxeio[i]
    list_char1.append(letter)

# COVERTING EACH LETTER TO ASCII NUMBER

l_char = len(list_char1)
list_ascii = []
for i in range(0,l_char):
    number = ord(list_char1[i])
    list_ascii.append(number)

# FINDING THE ODD NUMBERS AND CREATE A NEW LIST WITH THE LETTER FROM EACH NUMBER

list_monoi = []
list_char2 = []
for i in range(0,l):
    if list_ascii[i] % 2 != 0 :
        monos = list_ascii[i]
        list_monoi.append(monos)
        list_char2.append(list_char1[i])


# FINDING THE QYANTITY OF EACH LETTER IN THE LIST
# REMOVE IT FROM THE LIST EACH TIME IT WILL APPEAR AND REPLACE IT WITH " "
#FINALLY FIND THE RATE ROUND IT AND PRINT IT WITH *

length_char2 = len(list_char2)
for i in range(0 , length_char2):
    letter1 = list_char2[i]
    k = 0
    if list_char2[i] != "" :
        letter2 = ""
        for m in range(length_char2):
             if letter1 == list_char2[m]:
                     k = k + 1
                     position = m
                     list_char2.remove(list_char2[m])
                     list_char2.insert(position, letter2)
        pososto = k / length_char2 * 100
        p = round(pososto) + 1
        print(letter1 + ": " + p * "*" + "" + " " + str(p) + "%")