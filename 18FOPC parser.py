from pyparsing import Word, alphas, OneOrMore, ZeroOrMore, Forward, Group, Suppress

# Define FOPC grammar
identifier = Word(alphas, alphas + "_", asKeyword=True)
variable = Word(alphas.lower(), alphas.lower() + "_", asKeyword=True)
term = variable | identifier
expr = Forward()
arg_list = Suppress("(") + Group(OneOrMore(term + ZeroOrMore(Suppress(",") + term))) + Suppress(")")
expr << (identifier + arg_list) | variable

# Example FOPC expressions
expr1 = "isHuman(john)"
expr2 = "parentOf(john, alice)"
expr3 = "hasColor(apple, red)"

# Parse FOPC expressions
parsed_expr1 = expr.parseString(expr1, parseAll=True)
parsed_expr2 = expr.parseString(expr2, parseAll=True)
parsed_expr3 = expr.parseString(expr3, parseAll=True)

# Print parsed expressions
print(parsed_expr1.asList())
print(parsed_expr2.asList())
print(parsed_expr3.asList())
     
