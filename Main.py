import Functions as fun

#Read the Source Code Line by line
Code =open("test.txt", "r")

for line in Code:
    fun.CheckToken(line)
