import ply.yacc as yacc

from lex2 import tokens


def p_expression(p):
    '''expression : NUMBER'''
    p[0] = p[1]

operations = {
    '+' : lambda x,y : x+y,
    '-' : lambda x,y : x-y,
    '*' : lambda x,y : x*y,
    '/' : lambda x,y : x/y
}

def p_expression_op(p):
    '''expression : expression ADD_OP expression
        | expression MUL_OP expression'''
    p[0] = operations[p[2]](p[1],p[3])

def p_error(p):
    print("Syntax error in line %d" %p.lineno)
    parser.errok()

parser = yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    print(result)