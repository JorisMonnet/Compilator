import AST
from AST import addToClass
from functools import reduce
from parser5 import parse
import sys


operations = {
    '+' : lambda x,y : x+y,
    '-' : lambda x,y : x-y,
    '*' : lambda x,y : x*y,
    '/' : lambda x,y : x/y,
}
vars = {}

@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        c.execute()

@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            print(f"Error : Variable {self.tok} undefined !")
    return self.tok

@addToClass(AST.OpNode)
def execute(self):
    args = [c.execute() for c in self.children]
    if len(args) == 1:
        args.insert(0,0)
    return reduce(operations[self.op], args)

@addToClass(AST.AssignNode)
def execute(self):
    vars[self.children[0].tok] = self.children[1].execute()

@addToClass(AST.PrintNode)
def execute(self):
    print(self.children[0].execute())

@addToClass(AST.WhileNode)
def execute(self):
    while(self.children[0].execute()):
        self.children[1].execute()

if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    ast.execute()