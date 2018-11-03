reservedTokens=["write", "read", "if", "end", "while", "do", "repeat", ";"]
listOfRelationalOperators  = ["<", ">", "<=", ">=", "==", "<>", ":="]
listOfArthmitic = ["(", ")", "+", "-", "*", "/"]

def DFA(line):
    ListOfChar = list(line)
    while (len (ListOfChar) > 0):
        # print(" ListOfChar[0]= ",ListOfChar[0])
        if ListOfChar[0] == "{":
            state = "INCOMMENT"
            # switcher(ListOfChar, state)
        elif ListOfChar[0] == " ":
            state = "Start"
            print("Space")
            # switcher(ListOfChar, state)
        elif (ListOfChar[0].isdigit()):
            state = "INNUM"
        elif (ListOfChar[0].isalpha()):
            state = "INID"
        elif(ListOfChar[0]==":"):
             state = "INASSIGN"
        else:
            print("error")
            print(ListOfChar[0])
            ListOfChar.clear()
        switcher(ListOfChar, state)


def switcher(ListOfChar, state):
    if(state == "Start"):
        if len(ListOfChar) == 0:
             return
        elif len(ListOfChar) > 0:
            if ListOfChar[0] == " ":
               ListOfChar.pop(0)
               print("Space")


            DFA(str(ListOfChar))
    elif (state == "INNUM"):
        digit = ListOfChar.pop(0)
        character=""
        while (digit.isdigit()):
            character += digit
            digit = ListOfChar.pop(0)
        print(character, " Number")
        switcher(ListOfChar, "Done")

    elif (state == "INID"):
        char = ListOfChar.pop(0)
        character = ""
        while (char.isalpha()):
            character += char
            char= ListOfChar.pop(0)
        print(character, " Identifier")
        switcher(ListOfChar, "Start")

    elif (state == "INASSIGN"):
        if(ListOfChar[1]=="="):
            assign=ListOfChar.pop(0)+ListOfChar.pop(0)
            print(assign, " Assign")
            DFA(str(ListOfChar))

    elif (state == "INCOMMENT"):
        comment = ""
        while (ListOfChar[0] != "}"):
            comment = comment + ListOfChar[0]
            ListOfChar.pop(0)
        comment = comment + ListOfChar[0]
        ListOfChar.pop(0)
        print(comment+" Comment")
        switcher(ListOfChar, "Start")

    elif (state == "DONE"):
        switcher(ListOfChar, "Start")

