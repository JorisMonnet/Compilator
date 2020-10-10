# -*- coding: utf-8 -*-

" Infos ! La fonction debug(f) est un décorateur "
def debug(f):
    def inner(*args):
        print(f.__name__ + " : " + str(LATok.value))
        '''
        Infos ! Explorez :
            - La variable "LATok"
            - "f.__name__", qui donne le nom de la fonction f passée en argument
            - Les arguments "args"
        '''
    return inner

from ply import lex
import sys

tokens = [
    'IDENTIFIER'
    ]
    
literals = '()+'

t_IDENTIFIER = r'\w+'

def t_error(t):
    print ("Bad char!")

@debug
def token(t):
    global LATok
    if not LATok :
        return t == 'EOF'
    if LATok.type != t :
        return False
    LATok = lex.token()
    return True

@debug
def require(found):
    if found : 
        return True
    error("Error while parsing near token %s" %LATok.value)

@debug
def input():
    return expression() and require(token('EOF'))

@debug
def expression():
    return term() and require(rest_expression())

@debug
def term():
    return token('identifier') or parenth_expr()

@debug
def parenth_expr():
    return token('(') and require(expression()) and require(token(')'))

@debug
def rest_expression():
    return (token('+') and require(expression()))or True

lex.lex()

if __name__ == '__main__':
    input_str = '12+3'
    global LATok
    print ("** parsing: ", input_str)
    lex.input(input_str)
    LATok = lex.token() # Read the first token from lexical analyser
    result = input() # Start parsing 
    print ("** result: ", result)
    
    

    
