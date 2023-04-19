# Brainfuck Interpreter in Python

This is a simple interpreter for the Brainfuck programming language, written in Python. The interpreter takes a file containing Brainfuck code as input and executes it.

## Requirements

To run the interpreter, you need to have Python installed on your computer. You can download Python from the official website [here](https://www.python.org/downloads/).

You'll also need to install the [numpy library](https://pypi.org/project/numpy/)

## Usage

To use the interpreter, simply run the following command:

```
python bf.py <filename>
```


Replace `<filename>` with the name of the file containing the Brainfuck code that you want to execute.

For example, if you have a file called `hello.bf` containing the following code:

```
>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-]<+.
```

You can run the interpreter with the following command:

```
python bf.py hello.bf
```

and the output should be `Hello, World!`
