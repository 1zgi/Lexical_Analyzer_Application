import regex as re

INPUT_PATH = "file.txt"

KEYWORDS = {"for": "FOR",
            "while": "WHILE",
            "if": "IF",
            "else": "ELSE",
            "|": "BITWISE_OR",
            "||": "LOGICAL_OR",
            "&": "BITWISE_AND",
            "&&": "LOGICAL_AND"}


class Token:

    def __init__(self, token, integer_value=None, float_value=None, index=None, unrecognized_string=None):

        self.token = token
        self.integer_value = integer_value
        self.float_value = float_value
        self.index = index
        self.unrecognized_string = unrecognized_string

    def __str__(self):
        if self.token == "INTEGER":
            return "<token={}, integer_value = {}>".format(self.token, self.integer_value)
        elif self.token == "FLOAT":
            return "<token={}, float_value = {}>".format(self.token, self.float_value)
        elif self.token == "ID":
            return "<token={}, index = {}>".format(self.token, self.index)
        elif self.token == "ERROR":
            return "<token={}, unrecognized_string = {}>".format(self.token, self.unrecognized_string)
        else:
            return "<token={}>".format(self.token)

    def lexer(self, contents):  # splits the contents into tokens
        lines = contents.split("\n")
        for line in lines:
            chars = list(line)  # list function puts every character inside a line an array
            tokens = []
            temp_str = ""
            quote_count = 0  # This variable counts the occurrence of quotation marks(" or ') encountered in the loop.
            for char in chars:
                if chars == '"' or char == "'":
                    quote_count += 1
                if quote_count % 2 == 0:  # checks even or odd
                    in_quotes = False  # This variable is set to False if the current position is outside a quoted
                    # string (when quote_count is even), otherwise, it's set to True.
                else:
                    in_quotes = True

                if char == " " and in_quotes == False:
                    tokens.append(temp_str)
                    temp_str = ""
                else:
                    temp_str += char
            tokens.append(temp_str)
            items = []  # token list
            for token in tokens:
                if token[0] == '"' or token[0] == "'":  # checking...Is it string ?
                    if token[-1] == '"' or token[-1] == "'":  # gives last letter of string
                        items.append(("string", token))
                    else:
                        # Throw Error
                        break
                elif re.match("ID", token):  # checking...Is it identifier ?
                    items.append(("identifier", token))
                elif token in "+-*/":  # a+1 => gives Error
                    items.append(("expression", token))
                elif re.match(r"[.0-9]+", token):  # checking...Is it number ?
                    items.append(("number", token))
            return items

    def parse(self):  # reads the file and returns the string
        contents: str = open(INPUT_PATH, "r").read()
        tokens = self.lexer(contents)
        return tokens

# String " " or ' '
# Symbol ex: print function var
# Expression +-/*
# Number 0-9
