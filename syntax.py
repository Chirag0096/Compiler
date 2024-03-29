from sly import Parser
from lexer import MyLexer

class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('statement_list')
    def program(self, p):
        return ('program', p.statement_list)

    @_('statement')
    def statement_list(self, p):
        return [p.statement]

    @_('statement statement_list')
    def statement_list(self, p):
        return [p.statement] + p.statement_list

    @_('expression')
    def statement(self, p):
        return p.expression




    @_('expression PLUS term')
    def expression(self, p):
        return ('plus', p.expression, p.term)

    @_('expression MINUS term')
    def expression(self, p):
        return ('minus', p.expression, p.term)

    @_('term')
    def expression(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return ('times', p.term, p.factor)

    @_('term DIVIDE factor')
    def term(self, p):
        return ('divide', p.term, p.factor)

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return ('number', p.NUMBER)

    @_('LPAREN expression RPAREN')
    def factor(self, p):
        return p.expression
    @_('IDENTIFIER')
    def factor(self, p):
        return ('identifier', p.IDENTIFIER)
    @_('IDENTIFIER ASSIGN expression')
    def expression(self, p):
        return ('assignment', p.IDENTIFIER, p.expression)
    # ... other grammar rules

parser = MyParser()
source_code = input("Enter your code: ")
