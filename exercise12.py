file = input("give an ascii file ")
for i in range(len(file)):
    letter = file[len(file)-i -1] # TAKING THE CHARACTERS FROM THE END TO START
    number = ord(letter) # CONVERTING INTO NUMBERS
    number2 = 128 - number # FINDING SPECULAR NUMBERS
    ascii = chr(number2) # CONVERTING INTO CHARACTER
    print(ascii , end ="") # PRINT THE TEXT