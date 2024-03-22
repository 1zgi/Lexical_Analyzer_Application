class SymbolTable:
    count = 3

    def __init__(self):
        self.table = {"FOR": 0,
                      "WHILE": 1,
                      "IF": 2,
                      "ELSE": 3}
        self.inverse_table = {val: key for key, val in self.table.items()}  # keeping inverse of table

    def add(self, identifier):
        if identifier in self.table:
            return self.table[identifier]

        # update the tables
        self.count += 1
        self.table[identifier] = self.count
        self.inverse_table[self.count] = identifier

        return self.count

    def __str__(self):
        header = "--- SYMBOL TABLE ---\n"

        return header + "\n".join([
            "{} -> {}".format(key, val) for key, val in self.inverse_table.items()
        ])
