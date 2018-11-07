import Function as fun

#Read the Source Code Line by line

Code = "{Sample program in TINY language Factorial}" \
       "factorial := 1;"\
       "count := x;"\
       " write  fact   {  output  factorial of x } "\
       "y := y +3 "\
       " read x;   {input an integer }"\
       "if  0 < x   then "\
       "{dont compute if x <= 0 }"\
       "fact  := 1;"\
       "repeat "\
       "fact  := fact *  x;            " \
       " x  := x  -  1         " \
       "until  " \
       "x  =  0;        " \
       " write  fact   {  output  factorial of x }" \
       "end"

fun.DFA(Code)
'''
f = open('Test.txt', 'r')
line=f.readlines()
for x in line:
       fun.DFA(x)
'''
