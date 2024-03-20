import regex as re

KEYWORDS = {"for": "FOR",
            "while": "WHILE",
            "if": "IF",
            "else": "ELSE",
            "|": "BITWISE_OR",
            "||": "LOGICAL_OR",
            "&": "BITWISE_AND",
            "&&": "LOGICAL_AND"}


class LexerResult:
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

    @staticmethod
    def lexer(tokens):  # splits the contents into tokens
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
            elif token in r"[+-*/]+":  # a+1 => gives Error
                items.append(("expression", token))
            elif re.match(r"[.0-9]+", token):  # checking...Is it number ?
                items.append(("number", token))
        return items
