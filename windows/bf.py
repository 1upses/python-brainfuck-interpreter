from lists import list
import sys, msvcrt

def open_file(filename):
    temp = ""
    string = ""
    with open(filename, "r") as f:
        temp = f.read()
    for char in temp:
        if char in "><+-.,[]":
            string += char
    if string.count("[") != string.count("]"):
        print("Error: unmatched brackets")
        sys.exit(1)
    return string

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python bf.py <filename>")
        sys.exit(1)

    string = open_file(sys.argv[1])
    pointer = i = 0
    array = list()

    while i < len(string):
        match string[i]:
            case ">":
                pointer += 1
            case "<":
                pointer -= 1
            case "+":
                array.increment(pointer)
            case "-":
                array.decrement(pointer)
            case ".":
                print(chr(array.get(pointer)), end="")
            case ",":
                array.set(pointer, ord(msvcrt.getch()))
            case "[":
                if array.get(pointer) == 0:
                    while string[i] != "]":
                        i += 1
            case "]":
                if array.get(pointer) != 0:
                    while string[i] != "[":
                        i -= 1
        i += 1

    sys.exit(0)
