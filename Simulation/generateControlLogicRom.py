output = [0] * pow(2, 12)
for i in range(len(output)):
    # Fetch-Cycle
    if((i >> 5) & 0b1111) == 0:
        output[i] = pow(2, 21) + pow(2, 24)
    elif((i >> 5) & 0b1111) == 1:
        output[i] = pow(2, 25) + pow(2, 27) + pow (2, 30)

    # LDA 2byte
    elif (i & 0b11111) == 1:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 10) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) >= 4:
            output[i] = pow(2, 31)
    # LDA 3 byte
    elif (i & 0b11111) == 2:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 5:
            output[i] = pow(2, 17) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 6:
            output[i] = pow(2, 20) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 7:
            output[i] = pow(2, 10) + pow(2, 25)
        elif((i >> 5) & 0b1111) >= 8:
            output[i] = pow(2, 31)
            
    # LDB 2byte
    elif (i & 0b11111) == 3:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 8) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) >= 4:
            output[i] = pow(2, 31)
    # LDB 3 byte
    elif (i & 0b11111) == 4:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 5:
            output[i] = pow(2, 17) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 6:
            output[i] = pow(2, 20) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 7:
            output[i] = pow(2, 8) + pow(2, 25)
        elif((i >> 5) & 0b1111) >= 8:
            output[i] = pow(2, 31)
            
    # STA
    elif (i & 0b11111) == 5:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 5:
            output[i] = pow(2, 17) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 6:
            output[i] = pow(2, 20) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 7:
            output[i] = pow(2, 9) + pow(2, 26)
        elif((i >> 5) & 0b1111) >= 8:
            output[i] = pow(2, 31)

    # STB
    elif (i & 0b11111) == 6:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 5:
            output[i] = pow(2, 17) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 6:
            output[i] = pow(2, 20) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 7:
            output[i] = pow(2, 7) + pow(2, 26)
        elif((i >> 5) & 0b1111) >= 8:
            output[i] = pow(2, 31)

    # SWP
    elif (i & 0b11111) == 7:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 17) + pow(2, 9)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 7) + pow(2, 10)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 8) + pow(2, 16)
        elif((i >> 5) & 0b1111) >= 5:
            output[i] = pow(2, 31)

    # ATC
    elif (i & 0b11111) == 8:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 9) + pow(2, 17)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # ATD
    elif (i & 0b11111) == 9:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 9) + pow(2, 19)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # JMP
    elif (i & 0b11111) == 10:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 5:
            output[i] = pow(2, 17) + pow(2, 25)
        elif((i >> 5) & 0b1111) == 6:
            output[i] = pow(2, 20) + pow(2, 22)
        elif((i >> 5) & 0b1111) >= 7:
            output[i] = pow(2, 31)
    
    # JMZ
    elif (i & 0b11111) == 11:
        if(i >> 10 & 0b1) == 1:
            if((i >> 5) & 0b1111) == 2:
                output[i] = pow(2, 21) + pow(2, 24)
            elif((i >> 5) & 0b1111) == 3:
                output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
            elif((i >> 5) & 0b1111) == 4:
                output[i] = pow(2, 21) + pow(2, 24)
            elif((i >> 5) & 0b1111) == 5:
                output[i] = pow(2, 17) + pow(2, 25)
            elif((i >> 5) & 0b1111) == 6:
                output[i] = pow(2, 20) + pow(2, 22)
            elif((i >> 5) & 0b1111) >= 7:
                output[i] = pow(2, 31)
        elif(i >> 5 & 0b1111) <= 3:
            output[i] = pow(2, 27)
        else:
            output[i] = pow(2, 31)

    # JMC
    elif (i & 0b11111) == 12:
        if(i >> 9 & 0b1) == 1:
            if((i >> 5) & 0b1111) == 2:
                output[i] = pow(2, 21) + pow(2, 24)
            elif((i >> 5) & 0b1111) == 3:
                output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
            elif((i >> 5) & 0b1111) == 4:
                output[i] = pow(2, 21) + pow(2, 24)
            elif((i >> 5) & 0b1111) == 5:
                output[i] = pow(2, 17) + pow(2, 25)
            elif((i >> 5) & 0b1111) == 6:
                output[i] = pow(2, 20) + pow(2, 22)
            elif((i >> 5) & 0b1111) >= 7:
                output[i] = pow(2, 31)
        elif(i >> 5 & 0b1111) <= 3:
            output[i] = pow(2, 27)
        else:
            output[i] = pow(2, 31)

    # JMN
    elif (i & 0b11111) == 13:
        if(i >> 11 & 0b1) == 1:
            if((i >> 5) & 0b1111) == 2:
                output[i] = pow(2, 21) + pow(2, 24)
            elif((i >> 5) & 0b1111) == 3:
                output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
            elif((i >> 5) & 0b1111) == 4:
                output[i] = pow(2, 21) + pow(2, 24)
            elif((i >> 5) & 0b1111) == 5:
                output[i] = pow(2, 17) + pow(2, 25)
            elif((i >> 5) & 0b1111) == 6:
                output[i] = pow(2, 20) + pow(2, 22)
            elif((i >> 5) & 0b1111) >= 7:
                output[i] = pow(2, 31)
        elif(i >> 5 & 0b1111) <= 3:
            output[i] = pow(2, 27)
        else:
            output[i] = pow(2, 31)

    # JSR
    elif (i & 0b11111) == 14:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 19) + pow(2, 25) + pow (2, 27)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 21) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 5:
            output[i] = pow(2, 17) + pow(2, 25) + pow(2, 27)
        elif((i >> 5) & 0b1111) == 6:
            output[i] = pow(2, 12) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 7:
            output[i] = pow(2, 15) + pow(2, 26) + pow(2, 28)
        elif((i >> 5) & 0b1111) == 8:
            output[i] = pow(2, 12) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 9:
            output[i] = pow(2, 15) + pow(2, 26) + pow(2, 29)
        elif((i >> 5) & 0b1111) == 10:
            output[i] = pow(2, 20) + pow(2, 22)
        elif((i >> 5) & 0b1111) >= 11:
            output[i] = pow(2, 31)

    # RTS
    elif (i & 0b11111) == 15:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 14)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 12) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 14) + pow(2, 17) + pow(2, 25)
        elif((i >> 5) & 0b1111) == 5:
            output[i] = pow(2, 12) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 6:
            output[i] = pow(2, 19) + pow(2, 25)
        elif((i >> 5) & 0b1111) == 7:
            output[i] = pow(2, 20) + pow(2, 22)
        elif((i >> 5) & 0b1111) >= 8:
            output[i] = pow(2, 31)

    # ADD
    elif (i & 0b11111) == 16:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 0) + pow(2, 3) + pow(2, 5) + pow(2, 6) + pow(2, 10) + pow(2, 11)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # SUB
    elif (i & 0b11111) == 17:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 1) + pow(2, 2) + pow(2, 6) + pow(2, 10) + pow(2, 11)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # SHL
    elif (i & 0b11111) == 18:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 2) + pow(2, 3) + pow(2, 5) + pow(2, 6) + pow(2, 10) + pow(2, 11)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # NOT
    elif (i & 0b11111) == 19:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 4) + pow(2, 6) + pow(2, 10) + pow(2, 11)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # AND
    elif (i & 0b11111) == 20:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 0) + pow(2, 1) + pow(2, 3) + pow(2, 4) + pow(2, 6) + pow(2, 10) + pow(2, 11)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # XOR
    elif (i & 0b11111) == 21:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 1) + pow(2, 2) + pow(2, 4) + pow(2, 6) + pow(2, 10) + pow(2, 11)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # OR
    elif (i & 0b11111) == 22:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 1) + pow(2, 2) + pow(2, 3) + pow(2, 4) + pow(2, 6) + pow(2, 10) + pow(2, 11)
        elif((i >> 5) & 0b1111) >= 3:
            output[i] = pow(2, 31)

    # PSH
    elif (i & 0b11111) == 23:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 12) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 9) + pow(2, 15) + pow(2, 26)
        elif((i >> 5) & 0b1111) >= 4:
            output[i] = pow(2, 31)

    # POP
    elif (i & 0b11111) == 24:
        if((i >> 5) & 0b1111) == 2:
            output[i] = pow(2, 14)
        if((i >> 5) & 0b1111) == 3:
            output[i] = pow(2, 12) + pow(2, 24)
        elif((i >> 5) & 0b1111) == 4:
            output[i] = pow(2, 10) + pow(2, 25)
        elif((i >> 5) & 0b1111) >= 5:
            output[i] = pow(2, 31)



# Write the generated array to a Logisim-Compatible file

def splitWord(word):
    split = []
    for i in range(4):
        split.append(word & 0xFF)
        word >>= 8
    return split

with open("ControlLogicROM", "wb") as f:
    for cell in output:
        f.write(bytes(splitWord(cell)))
