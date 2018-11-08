reservedTokens=["write", "read", "if", "end", "while", "do", "repeat", "until", "then"]
listOfRelationalOperators  = ["<", ">", "<=", ">=", "==", "<>","="]
listOfArthmitic = ["(", ")", "+", "-", "*", "/"]


def DFA(line):
    ListOfChar = list(line)
    while(len(ListOfChar) > 0):
        if ListOfChar[0] == "{":
            state = "INCOMMENT"
            # break
        elif (ListOfChar[0]  == "\""):
            state="String"
        elif (ListOfChar[0] in listOfArthmitic):
            state = "Operation"
        elif (ListOfChar[0] in listOfRelationalOperators):
            state = "Relation"
        elif (ListOfChar[0]  == ";"):
            state="End"
        elif (ListOfChar[0].isalpha()):
            state = "INID"
            # break
        elif (ListOfChar[0] == " "):
            state = "Start"
         #   print("ddd")
        elif (ListOfChar[0] == ":"):
            state = "INASSIGN"
        elif (ListOfChar[0].isdigit()):
            state = "INNUM"


        if (state == "INCOMMENT"):
            comment = ""
            while (ListOfChar[0] != "}"):
                comment = comment + ListOfChar[0]
                ListOfChar.pop(0)
            comment = comment + ListOfChar[0]
            ListOfChar.pop(0)
            print(comment + " Comment")
            state = "Start"

        elif (state == "INID"):
            char = ListOfChar.pop(0)
            character = ""
            while (char.isalpha()):
                character += char
                if(len(ListOfChar)<1 or ListOfChar[0] == ";" or ListOfChar[0] == "" or ListOfChar[0] == " "):
                    break
                else:
                    char = ListOfChar.pop(0)

            if(character in reservedTokens):
                print(character, " Reserved Word")
            else:
                print(character, " Identifier")
            state = "Start"

        elif (state == "Start"):
            print(ListOfChar[0])
            if len(ListOfChar) == 0:
                return
            elif len(ListOfChar) > 0:
                if ListOfChar[0] == " ":
                    ListOfChar.pop(0)


        elif (state == "INASSIGN"):
            if (ListOfChar[1] == "="):
                assign = ListOfChar.pop(0) + ListOfChar.pop(0)
                print(assign, " Assign")

        elif (state == "INNUM"):
            digit = ListOfChar.pop(0)
            character = ""
            while (digit.isdigit()):
                character += digit
                if (len(ListOfChar)<1 or ListOfChar[0] == ";" or ListOfChar[0] == "" or ListOfChar[0] == " "):
                    break
                else:
                    digit = ListOfChar.pop(0)
            print(character, " Number")

        elif (state == "Relation"):
            operation = ListOfChar.pop(0)
            checkop = operation+ListOfChar[0]
            if(checkop in listOfRelationalOperators):
                operation = operation+ListOfChar.pop(0)
            print (operation, " Relational Operation")

        elif (state == "Operation"):
            operation = ListOfChar.pop(0)
            print (operation, " Arithmetic Operation")

        elif (state == "End"):
            operation = ListOfChar.pop(0)
            print (operation, " End Token")

        elif (state == "String"):
            ListOfChar.pop(0)
            charStr = ListOfChar.pop(0)
            character = "\""
            while (charStr != "\""):
                character += charStr
                if (len(ListOfChar) < 1):
                    break
                else:
                    charStr = ListOfChar.pop(0)
            character+= "\""
            print(character, " String")