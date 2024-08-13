import sys
from meowlang.interpreter import interpret
from meowlang.repl import repl

if len(sys.argv) != 2:
    repl()
    exit(1)

path = sys.argv[1]
if not path.endswith('.purr'): print('Invalid file format. File must have a .purr extension.'); exit(1)

interpret(path)