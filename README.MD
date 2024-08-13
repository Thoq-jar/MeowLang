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
readstr
purr "Result: "
eval
clear
exit
```
Compare int:
```meowlang
readint
readint
sub
jump.eq.0 L1
purrln "Not equal!"
exit

L1:
purrln "equal"
exit
```


## License 
This project is licensed under the MIT license


# Cat
> Cats, as you know, are quite impervious to threats. -Connie Willis