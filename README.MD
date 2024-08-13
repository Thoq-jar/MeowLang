# Meowlang

> Meowlang is an esoteric programming language.

> Designed to be a fun project not meant for real-world use.

## Instalation

-   Step 1:

    Clone the repo with [git](https://git-scm.com/)

    ```bash
    git clone https://github.com/Thoq-jar/MeowLang.git
    ```

-   Step 2:

    Ensure python3 is installed!
    If not you can install it from [here](https://www.python.org/)!

-   Step 3 (OPTIONAL):

    Install [PyPy](https://pypy.org/) For the best performance (~2-20x faster)

-   Step 4:

    Run your code:

    With PyPy (Recomended):
    ```shell
    pypy3 meow.py examples/main.purr
    ```
    With python:
     ```shell
    python3 meow.py
    ```
    This will run a calculator application

- Step 5: Repl:
    
    Meowlang includes a repl interface, to launch it simply run:

    With PyPy (Recomended):
    ```shell
    pypy3 meow.py
    ```
    With python:
    ```shell
    python3 meow.py
    ```

# Samples
>Code samples

Calculator.purr
```meowlang
purr "Input an expression: "
watchstr
purr "Result: "
meow
clear
good.night
```

## Syntax explanation
`purr` - prints without a \n

`purrln` - prints with a \n

`watchstr` - takes in string input

`watchint` - takes in a integer input

`clear` - clears the stack

`good.night` - exits with return code '0'

`meow` - evaluates the current data in stack

`add` - adds a + b

`sub` - subtracts a - b

`mul` - multiplies a * b

`div` - divides a / b

`mod` - uses the modulo for a % b

`cat` - Handles pushing a number from the program onto the stack and then moves to the next instruction.

`leap.eq.0` - Handles a conditional jump based on whether the top value of the stack is zero. If it is zero, it jumps to a specific label; otherwise, it proceeds to the next instruction.

`leap.gt.0` - Handles a conditional jump based on whether the top value of the stack is greater than zero. If it is greater than zero, it jumps to a specific label; otherwise, it proceeds to the next instruction.

## License 
This project is licensed under the MIT license


# Cat
> Cats, as you know, are quite impervious to threats. -Connie Willis