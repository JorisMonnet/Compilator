if __name__ == '__main__':
    from parser5 import parse 
    import sys,os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0]+'.vm'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print(f"Wrote output to {name}")