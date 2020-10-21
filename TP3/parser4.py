import ply.yacc as yacc
import AST
from lex5 import tokens

def p_programme_expr(p):
    '''programme : statement ';' programme'''
    p[0]=AST.ProgramNode([p[1]]+p[3].children)
        
def p_programme_statement(p):
    '''programme : statement'''
    p[0]= AST.ProgramNode(p[1])
    
def p_statement(p):
    '''statement : assignation
        | expression
        | structure '''
    p[0] = p[1]

def p_statement_print(p):
    '''statement : PRINT expression'''
    p[0]= AST.PrintNode(p[2])

def p_structure(p):
    '''structure : WHILE expression '{' programme '}' '''
    p[0]=AST.WhileNode([p[2],AST.ProgramNode(p[4].children)])

def p_assign(p):
    '''assignation : IDENTIFIER "=" expression '''
    p[0] = AST.AssignNode([AST.TokenNode(p[1]),p[3]])
    
def p_expression_var(p):
    '''expression : IDENTIFIER'''
    p[0] = AST.TokenNode(p[1])

def p_expression(p):
    '''expression : NUMBER'''
    p[0] = AST.TokenNode(p[1])

precedence = (
    ('left','ADD_OP'),
    ('left','MUL_OP'),
    ('right', 'UMINUS'),  
)

def p_minus(p):
    '''expression : ADD_OP expression %prec UMINUS'''
    p[0]=AST.OpNode(p[1],[0,p[2]])

def p_expression_paren(p):
    """expression : '(' expression ')'"""
    p[0] = p[2]

def p_expression_op(p):
    '''expression : expression ADD_OP expression
        | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2],[p[1],p[3]])

def p_error(p):
    print("Syntax error in line %d" %p.lineno)
    parser.errok()

def parse(prog):
    return yacc.parse(prog)

parser = yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()
    result = parse(prog)
    print(result)
    import os
    graph = result.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0] + '−ast.pdf'
    graph.write_pdf(name)
    print("wrote ast to" , name)

   