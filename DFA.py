

def DFA(line):
    ListOfChar = list(line)
    while(len(ListOfChar)>0):
        character=ListOfChar.pop(0)
        if (character.isdigit()):
            state = "INNUM"
        elif(character.isalpha()):
            state="INID"
        else:
            state="INASSIGN"
        switcher(ListOfChar,state,character)


def switcher(ListOfChar,x,character):
    if(x=="INNUM"):
        digit=ListOfChar.pop(0)
        while(digit.isdigit()):
            character+=digit
            digit = ListOfChar.pop(0)
        print (character," Number")
        switcher(ListOfChar,"Done",digit)
    elif(x == "INID"):
        digit = ListOfChar.pop(0)
        while (digit.isalpha()):
            character += digit
            digit = ListOfChar.pop(0)
        print (character, " Identifier")
        switcher(ListOfChar, "Done", digit)
    #elif (x == "INASSIGN"):



