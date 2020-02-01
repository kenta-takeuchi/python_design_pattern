import collections
import math
import sys
import types


def main():
    quit = "Ctrl+Z,Enter" if sys.platform.startswith("win") else "Ctrl+D"
    prompt = "Enter an expression ({} to quit): ".format(quit)
    current = types.SimpleNamespace(letter="A")
    globalContext = global_context()
    localContext = collections.OrderedDict()
    while True:
        try:
            expression = input(prompt)
            if expression:
                calculate(expression, globalContext, localContext, current)
        except EOFError:
            print()
            break


def global_context():
    globalContext = globals().copy()
    for name in dir(math):
        if not name.startswith("_"):
            globalContext[name] = getattr(math, name)
    return globalContext


def calculate(expression, globalContext, localContext, current):
    try:
        result = eval(expression, globalContext, localContext)
        update(localContext, result, current)
        print(", ".join(["{}={}".format(variable, value)
                for variable, value in localContext.items()]))
        print("ANS={}".format(result))
    except Exception as err:
        print(err)


def update(localContext, result, current):
    localContext[current.letter] = result
    current.letter = chr(ord(current.letter) + 1)
    if current.letter > "Z":  # We only support 26 variables
        current.letter = "A"


if __name__ == "__main__":
    main()
