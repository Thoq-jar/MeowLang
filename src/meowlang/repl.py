from src.meowlang.interpreter import replInterpreter


def repl():
    print("Welcome to MeowLang repl!")
    print("If you meant to run a file, use 'meow <file>'")
    print("Type 'exit' to exit the repl")
    while True:
        try:
            replInput = input("Meowlang >>> ")
            if replInput == "exit":
                break
            if replInput == "":
                continue
            replInterpreter(replInput)
        except Exception as _:
            print("Syntax error!")
            continue
