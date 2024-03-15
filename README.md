CMSE 318 / CMPE 410 Principles of Programming Languages

Spring 2023-2024

Assignment 2 

#Lexical Analyzer Application#

To be done in groups of two. Pick your partner! 
The Task:
You will write a lexical analyzer in Python that recognizes integers, floating point numbers, 
identifiers, logic operators &, &&, | and ||, as well as reserved words “for”, “while”, “if” and 
“else”. Examples of integers are 354, -322, 0. Examples of floating point numbers are 3.243, 
0.003, -3.4 etc. (no exponent notation required, such as 3.2E4). Examples of identifiers are sum, 
x123, big_size, A12R etc. 

Your lexical analyzer function should read the input from a file, and return an object as a result 
each time it is called. The returned object should have attributes for (1) the token, (2) index into 
the symbol table, (3) value in case of an integer, (4) value in case of a floating point, and (5) 
string of characters in case of an unrecognized lexeme. 
The main program should first read the name of the input file, and enter a loop, with the 
following menu being displayed: 

- Call lex()
  
- Show symbol table
  
- Exit
  
"Exit" should end the program. 

"Call lex()" should call the lexical analyzer to get the next token, as well as additional 
information. In case of

o An identifier, a pointer to the symbol table (index into the symbol table) should be
returned as the extra information. Identifiers should be placed by lex() in the symbol
table the first time they are encountered.

o An integer, the actual value of the integer should be returned as the extra information

o A floating point number, the actual value of the number should be returned as the extra
information

The “show symbol table” option should print the contents of the symbol table on the screen. 
 
Spaces should be skipped in the input file. 
 The TOKENS that should be returned by the lexical analyzer are: 
 
o INTEGER

o FLOAT

o ID

o BITWISE_OR (for |)

o LOGICAL_OR (for ||)

o BITWISE_AND (for &)

o LOGICAL_AND (for &&)

o FOR

o WHILE

o IF

o ELSE

Define TOKENS as enumerations. 

Initialize your symbol table with the reserved words “for”, “while”, “if”, “else”, so that 
identifiers are placed in positions 4 and higher.

Sample file contents (you should have a different file with at least two of each kind of TOKEN, 
as well as at least three unrecognized strings): 

x 45 5.4 -33 size 34RR y1234 && for x while
The lexical analyzer ( lex() ) should return the following objects (only relevant attributes shown) 
one at a time, as it is called for the sample file: 

<token=ID, index=4> 
<token=INTEGER, integer_value = 45> 
<token=FLOAT, float_value = 5.4> 
<token=INTEGER, integer_value = -33> 
<token=ID, index=5> 
<token=ERROR, unrecognizded_string = “34RR”> 
<token=ID, index=6> 
<token=LOGICAL_AND> 
<token=FOR> 
<token=ID, index=4> 
<token=WHILE> 

Each time lex() is called, the information in the object that it returns should be printed on the 
screen. 

You can assume that all lexemes are separated by white space, such as the space character, the 
tab character or a new line character. 

Hint: define a class for the return type of lex() that can hold different kinds of information, such 
as LEX_RESULT. 

What to hand in on Teams
o A report (pdf document). If your program does not work 100%, still write a report showing
the parts that do work. The report should contain

o the names of both partners (unless the project was done by a single student)

o brief description of what the project is about

o screenshots taken as the program is running to demonstrate that the program works
correctly for different cases

o the input text file

o commented source code, where you explain what each function / method does.

o Source code (a separate file of Python code)
