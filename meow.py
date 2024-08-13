import sys
from src.meowlang.interpreter import interpret
from src.meowlang.repl import repl

if len(sys.argv) != 2:
    repl()
    exit(1)

path = sys.argv[1]
if not path.endswith(".purr") and not path.endswith(".meow") and not path.endswith(".🐱"):
    print("Invalid file format! File must have a .purr, .meow or .🐱 extension.")
    exit(1)

interpret(path)
