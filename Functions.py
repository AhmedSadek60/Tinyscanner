
listOfTokens = ["while", "if", "else", "do", "end"]
listOfInputOutput = ["write", "read"]
listOfRelationalOperators = ["<", ">", "<=", ">=", "=", "<>"]
listOfArthmitic = ["(", ")", "+", "-", "*", "/"]

def CheckToken(line):
    if line.find('{') > -1:
        begin = line.index('{')
        endOfbBegin = line.index('}')
        comment = line[begin:endOfbBegin+1]
        print(comment,"Comment;")

        # To check if it's an output
    elif (line.find('write') > -1) :
        ListLine = line.split()
        for word in ListLine:
            if word in listOfInputOutput:
                print(word, "Input/ output statment;")
            elif word.find("\""):
                begin = line.index('"')
                while(word[begin+1:].find("\"") == -1):
                    word=word+" "+ListLine.pop(1)
                endOfbBegin = word[begin:].index('"')
                comment = word[begin:endOfbBegin + 1]
                print(comment, "String;")
            elif word[0].isalpha():
                print(word, "identifier;")
            else:
                print(word,"ERROR")

    # To check if it's an input
    elif (line.find('read') > -1):
        ListLine = line.split()
        for word in ListLine:
            if word in listOfTokens:
                print(word, "Control Statement;")
            elif word.find("\""):
                print(word, "String;")
            elif word[0].isalpha():
                print(word, "identifier;")
            elif word in listOfRelationalOperators:
                print(word, "Relational operator;")
            elif word.isdigit():
                print(word, "Number;")
            else:
                print("Error")

    # To check if it's a control statement
    elif (line.find('if') > -1) or (line.find('while') > -1) or (line.find('end') > -1) or (line.find('do') > -1):
        ListLine = line.split()
        for word in ListLine:
            if word in listOfTokens:
                print(word, "Control Statement;")
            elif word.find("\""):
                print(word, "String;")
            elif word[0].isalpha():
                print(word, "identifier;")
            elif word in listOfRelationalOperators:
                print(word, "Relational operator;")
            elif word.isdigit():
                print(word, "Number;")
            else:
                print("Error")
     #To check if it's an identifier
    elif (line[0].isalpha()) and (line.find(":=") > -1):
        ListLine = line.split()
        for word in ListLine:
            if word[0].isalpha():
                print(word, "identifier;")
            elif word in listOfRelationalOperators:
                print(word, "Relational operator;")
            elif word.isdigit():
                print(word, "Number;")





