from sly import Lexer

class MyLexer(Lexer):
    # Define your own token names
    tokens = { IDENTIFIER, NUMBER, PLUS, MINUS, TIMES, DIVIDE,
               ASSIGN, PRINT, LPAREN, RPAREN, STRING, COMMENT }
    ignore = ' \t'  # Ignore spaces and tabs
    # Regular expression rules for tokens
    IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9]*'
    NUMBER = r'\d+(\.\d+)?'  # Match integers and floats
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    PRINT = r'print'
    LPAREN = r'\('
    RPAREN = r'\)'
    STRING = r'\".*?\"'  # Match string literals
    COMMENT = r'\#.*'  # Match comments
    
    
    def __init__(self):
        self.lineno = 1  # Line number
        self.column = 1  # Column number

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')
        self.column = 1

    def track_position(self, t):
        self.column += len(t.value)

    # In your token rules, add this line:
    # self.track_position(t)
    

        # Additional rules
    @_(r'\n+')
    def newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1
        
lexer = MyLexer()
# Input statement
source_code = input("Enter your code: ")
# Tokenize the input
tokens = lexer.tokenize(source_code)
# Print the tokens
for token in tokens:
    print(token)
