import sys, re

if __name__ == "__main__":
    reg = re.compile(sys.argv[1])
    for line in open(sys.argv[2],"r"):
        if reg.search(line) : print(line)