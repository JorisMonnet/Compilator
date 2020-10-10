import ply.lex as lex

tokens = (
    'NUMBER',
    'ADD_OP',
    'MUL_OP'
)
t_ADD_OP = r'[\+-]'
t_MUL_OP = r'[\*/]'
literals = r'\(\)'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_newLine(t):
    r'\n'
    t.lexer.lineno += len(t.value)

t_ignore =' \t'

def t_error(t):
    print("Illegal character '%s'"% t.value[0])
    t.lexer.skip(1)
lex.lex()

if __name__ == "__main__":
    import sys 
    prog = open(sys.argv[1]).read()
    lex.input(prog)
    while 1 :
        tok = lex.token()
        if not tok : break
        print("line %d : %s(%s)"%(tok.lineno,tok.type,tok.value))
        