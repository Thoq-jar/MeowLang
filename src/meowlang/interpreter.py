from src.meowlang.stack import Stack


def read_file(program_filepath):
    with open(program_filepath, "r") as program_file:
        return [line.strip() for line in program_file.readlines()]


def parser(program_lines):
    program = []
    token_counter = 0
    label_tracker = {}

    for line in program_lines:
        parts = line.split(" ")
        opcode = parts[0]

        if opcode == "":
            continue

        if opcode.endswith(":"):
            label_tracker[opcode[:-1]] = token_counter
            continue

        program.append(opcode)
        token_counter += 1

        match opcode:
            case "cat":
                number = int(parts[1])
                program.append(number)
                token_counter += 1
            case "purr":
                string_literal = " ".join(parts[1:])[1:-1]
                program.append(string_literal)
                token_counter += 1
            case "purr!":
                string_literal = " ".join(parts[1:])[1:-1]
                program.append(string_literal)
                token_counter += 1
            case "leap.eq.0":
                label = parts[1]
                program.append(label)
                token_counter += 1
            case "leap.gt.0":
                label = parts[1]
                program.append(label)
                token_counter += 1

    return program, label_tracker


def execute(opcode, program, pc, stack, label_tracker):
    match opcode:
        case "cat":
            number = program[pc]
            stack.push(number)
            pc += 1
        case "pop":
            stack.pop()
        case "add":
            a = stack.pop()
            b = stack.pop()
            stack.push(a + b)
        case "sub":
            a = stack.pop()
            b = stack.pop()
            stack.push(b - a)
        case "mul":
            a = stack.pop()
            b = stack.pop()
            stack.push(a * b)
        case "div":
            a = stack.pop()
            b = stack.pop()
            stack.push(b // a)
        case "mod":
            a = stack.pop()
            b = stack.pop()
            stack.push(b % a)
        case "meow":
            expression = stack.pop()
            try:
                result = eval(expression)
                stack.push(result)
                print(result)
            except Exception as e:
                print(f"Error running eval!: {e}")
                return pc
        case "purr":
            string_literal = program[pc]
            print(string_literal, end="")
            pc += 1
        case "purr!":
            string_literal = program[pc]
            print(string_literal)
            pc += 1
        case "watchstr":
            input_string = str(input())
            stack.push(input_string)
        case "watchint":
            input_int = int(input())
            stack.push(input_int)
        case "leap.eq.0":
            number = stack.top()
            if number == 0:
                pc = label_tracker[program[pc]]
            else:
                pc += 1
        case "leap.gt.0":
            number = stack.top()
            if number > 0:
                pc = label_tracker[program[pc]]
            else:
                pc += 1
        case "clear":
            stack.sp = -1
        case _:
            print("Syntax error!")
            exit(1)

    return pc


def interpret(program_filepath):
    program_lines = read_file(program_filepath)
    program, label_tracker = parser(program_lines)

    pc = 0
    stack = Stack(256)

    while program[pc] != "good.night":
        opcode = program[pc]
        pc += 1
        pc = execute(opcode, program, pc, stack, label_tracker)


def replInterpreter(code):
    program_lines = code.split("\n")
    program, label_tracker = parser(program_lines)
    pc = 0
    stack = Stack(256)

    while pc < len(program) and program[pc]:
        opcode = program[pc]
        pc += 1
        pc = execute(opcode, program, pc, stack, label_tracker)
