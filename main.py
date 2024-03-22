from Token import *
from LexerResult import *
from SymbolTable import *

token = Token
tokens = token.parse("file.txt")
lex = LexerResult(tokens)


print("1. Call lex()")
print("2. Show symbol table")
print("3. Exit")

for i, token in enumerate(tokens):
    chosen_option = input("Choose one option:")
    if chosen_option == "3":
        break
    elif chosen_option == "2":
        print(symbol_table)
    elif chosen_option == "1":
        result = lex.lexer(tokens)
        for obj in result:
            print(obj)
    else:
        print("ERROR: invalid option!")
