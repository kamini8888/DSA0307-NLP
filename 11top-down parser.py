class Grammar:
    def __init__(self, productions):
        self.productions = productions

    def get_productions(self, non_terminal):
        return self.productions.get(non_terminal, [])

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        self.input_string = input_string
        self.index = 0
        self.current_token = None
        self.current_production = None
        self.tokens = self.tokenize(input_string)
        return self.parse_non_terminal('S')

    def tokenize(self, input_string):
        # Split input_string into tokens (assuming space-separated)
        return input_string.split()

    def next_token(self):
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            self.index += 1
            return self.current_token
        else:
            return None

    def parse_non_terminal(self, non_terminal):
        productions = self.grammar.get_productions(non_terminal)
        for production in productions:
            if self.try_production(production):
                return True
        return False

    def try_production(self, production):
        for symbol in production:
            if symbol.isupper():
                if not self.parse_non_terminal(symbol):
                    return False
            else:
                token = self.next_token()
                if token != symbol:
                    return False
        return True

# Example usage:
grammar = Grammar({
    'S': [['NP', 'VP']],
    'NP': [['the', 'cat'], ['the', 'dog']],
    'VP': [['sat'], ['ran']]
})

parser = Parser(grammar)
input_string = "the cat sat"
result = parser.parse(input_string)
print("Parsing Successful:", result)
