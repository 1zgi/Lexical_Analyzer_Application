class SymbolTable:
    count = 3

    def __init__(self):
        self.table = {"FOR": 0,
                      "WHILE": 1,
                      "IF": 2,
                      "ELSE": 3}
        # keeping inverse table ease the process of printing SymbolTable
        self.inv_table = {val: key for key, val in self.table.items()}

    def insert(self, identifier):
        if identifier in self.table:
            return self.table[identifier]

        # update the tables
        self.count += 1
        self.table[identifier] = self.count
        self.inv_table[self.count] = identifier

        return self.count

    def __str__(self):
        headline = "--- SYMBOL TABLE ---\n"

        return headline + "\n".join([
            "{} -> {}".format(key, val) for key, val in self.inv_table.items()
        ]) + "\n" + "-" * 10
