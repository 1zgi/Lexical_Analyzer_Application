import regex as re

class Token:

    INTEGER = 1
    FLOAT = 2
    ID = 3
    BITWISE_OR = 4
    LOGICAL_OR = 5
    BITWISE_AND = 6
    LOGICAL_AND = 7
    FOR = 8
    WHILE = 9
    IF = 10
    ELSE = 11

# Define reserved words and initialize symbol table
RESERVED_WORDS = {
    "for": Token.FOR,
    "while": Token.WHILE,
    "if": Token.IF,
    "else": Token.ELSE
}
symbol_table = RESERVED_WORDS.copy()
next_id = len(RESERVED_WORDS) + 1

    TOKEN_Pattern = [
        (Token.INTEGER, r'\d+'),  # Matches integers
        (Token.FLOAT, r'\d+\.\d+'),  # Matches floating-point numbers
        (Token.BITWISE_OR, r'\|'),  # Matches bitwise OR
        (Token.LOGICAL_OR, r'\|\|'),  # Matches logical OR
        (Token.BITWISE_AND, r'&'),  # Matches bitwise AND
        (Token.LOGICAL_AND, r'&&'),  # Matches logical AND
        (Token.ID, r'[a-zA-Z_][a-zA-Z0-9_]*')  # Matches identifiers
    ]

    def lexer(contents): # splits the contents into tokens
        lines = contents.split("\n")
        for line in lines:
            chars = list(line) # list function puts every character inside a line an array
            tokens = []
            temp_str = ""
            quote_count = 0 # This variable counts the occurrence of quotation marks(" or ') encountered in the loop.
            for char in chars:
                if chars == '"' or char == "'":
                    quote_count += 1
                if quote_count %2 == 0: # checks even or odd
                    in_quotes = False #This variable is set to False if the current position is outside a quoted string (when quote_count is even), otherwise, it's set to True.
                else:
                    in_quotes = True

                if char == " " and in_quotes == False:
                    tokens.append(temp_str)
                    temp_str = ""
                else:
                    temp_str +=char
            tokens.append(temp_str)
            items = []
            for token in tokens:
                if token[0] == '"' or token[0] == "'": # checking...Is it string ?
                    if token[-1] == '"' or token[-1] == "'": # gives last letter of string
                        items.append(("string",token))
                    else:
                        # Throw Error
                         break
                elif re.match("Token.ID",token): # checking...Is it identifier ?
                    items.append(("identifier",token))
                elif token in "+-*/": # a+1 => gives Error
                    items.append(("expression",token))
                elif re.match(r"[.0-9]+", token):
                    items.append(("number" , token))
            return items


    def parse(file): # reads the file and returns the string
        contents: str = open(file,"r").read()
        tokens = lexer(contents)
        return tokens

# String " " or ' '
# Symbol ex: print function var
# Expression +-/*
# Number 0-9



