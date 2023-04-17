from linked_lists import linked_list
import sys, tty, termios

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
    array = linked_list()

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
                old_settings = termios.tcgetattr(sys.stdin.fileno())
                tty.setcbreak(sys.stdin.fileno())
                array.set(pointer, ord(sys.stdin.read(1)))
                termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
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
