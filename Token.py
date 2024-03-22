class Token:

    @staticmethod
    def tokenize(contents):
        lines = contents.split("\n")
        tokens = []
        for line in lines:
            chars = list(line)  # list function puts every character inside a line an array
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

                if char == " " and not in_quotes:
                    tokens.append(temp_str)
                    temp_str = ""
                else:
                    temp_str += char
            tokens.append(temp_str)
        return tokens

    @staticmethod
    def parse(file):  # reads the file and returns the string
        contents: str = open(file, "r").read()
        tokens = Token.tokenize(contents)
        return tokens

