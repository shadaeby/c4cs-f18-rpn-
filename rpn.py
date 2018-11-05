#!/usr/bin/env python3

import operator
#import colorama
#from colorama import *
#from colorama import Fore, Back, Style

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
  #  init();
 #   print(Fore.RED + "This is red text");

 #   print(Fore.RED + 'some red text')
  #  print(Back.GREEN + 'and with a green background')
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()

