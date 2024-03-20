import re

KEYWORDS = {"for": "FOR",
            "while": "WHILE",
            "if": "IF",
            "else": "ELSE",
            "|": "BITWISE_OR",
            "||": "LOGICAL_OR",
            "&": "BITWISE_AND",
            "&&": "LOGICAL_AND"}


class LexerResult:
    def __init__(self, token=None, integer_value=None, float_value=None, index=None, unrecognized_string=None):

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
    def is_int_float(number):
        try:
            number = int(number)
            return "INTEGER", number
        except ValueError:
            try:
                number = float(number)
                return "FLOAT", number
            except ValueError:
                return None, None

    @staticmethod
    def check_identifier(token):
        return KEYWORDS.get(token)

    def lexer(self, tokens):  # splits the contents into tokens
        lex_result = self.analyzer(tokens)
        return lex_result

    def analyzer(self, tokens):
        items = []  # token list
        for token in tokens:
            if token[0] == '"' or token[0] == "'":  # checking...Is it string ?
                if token[-1] == '"' or token[-1] == "'":  # gives last letter of string
                    items.append(("string", token))
                else:
                    # Throw Error
                    break
            elif re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$", token):  # checking...Is it identifier ?
                idx = self.check_identifier(token)
                if idx:
                    items.append(("ID", idx))
                else:
                    items.append(("ID", token))
            elif token in "+-*/+":  # a+1 => gives Error
                items.append(("EXPRESSION", token))
                # self.check_expression(token)
            elif re.match(r"[.0-9]+", token):  # checking...Is it number ?
                var_type, var_value = self.is_int_float(token)
                if var_type:
                    items.append((var_type, var_value))
            else:
                items.append(("ERROR", token))

        return items