import Function as fun
# Open the file with read only permit
f = open('test.txt')
# use readline() to read the first line
line = f.readline()

while line:
    fun.DFA(line.split("\n")[0])
    # use realine() to read next line
    line = f.readline()
f.close()