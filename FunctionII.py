reservedTokens=["write", "read", "if", "end", "while", "do", "repeat", ";"]
listOfRelationalOperators  = ["<", ">", "<=", ">=", "==", "<>", ":="]
listOfArthmitic = ["(", ")", "+", "-", "*", "/"]


def DFA(line):
    ListOfChar = list(line)
    while(len(ListOfChar) > 0):
        if ListOfChar[0] == "{":
            state = "INCOMMENT"
            # break

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
                char = ListOfChar.pop(0)
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
                digit = ListOfChar.pop(0)
            print(character, " Number")