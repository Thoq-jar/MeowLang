# Meowlang

> Meowlang is an esoteric programming language.

> Designed to be a fun project not meant for real-world use.

## Instalation
> How to install and run
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
    ```bash
    pypy3 meow.py examples/main.purr
    ```
    With python:
     ```bash
    python3 meow.py
    ```
    This will run a calculator application

- Step 5: Repl:
    
    Meowlang includes a repl interface, to launch it simply run:

    With PyPy (Recomended):
    ```bash
    pypy3 meow.py
    ```
    With python:
    ```bash
    python3 meow.py
    ```

# First Meowlang program
> Basic 'Hello, World' program
- Step 1

    Create a file with a .purr, .meow or .🐱 extension.

- Step 2:
    
    Put this in the file
    ```meowlang
    purr! "Hello, Cats!"
    good.night
    ```
- Step 3:

    Run the program (extenstion changes based on your choice above)
    ```bash
    pypy3 meow.py cat.🐱 
    ```
    ```bash
    pypy3 meow.py cat.purr
    ```
    ```bash
    pypy3 meow.py cat.meow
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
> What the syntax is and what it does

`purr` - prints without a \n

`purrr` - prints with a \n

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
> License for Meowlang

This project is licensed under the MIT license


## Cat
> Cats, as you know, are quite impervious to threats. -Connie Willis

## Credits
> This project is based on [bvdl.io's](https://github.com/basvdl97) interpreter 
from [this git repo](https://github.com/basvdl97/OLL-Interpreter). 

> They have a tutorial to make your own fun language [here](https://www.youtube.com/watch?v=A3gTw1ZkeK0&t=150s)!

> You should watch is as it containes a lot of good information!