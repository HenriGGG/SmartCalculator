# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:25:37 2020

@author: Harry
"""

# main python proghram
import math
import random

response = [
    'Welcome to smart calculator',
    'YOUR NAME HERE',
    'Thanks for enjoy with me',
    'Sorry ,this is  beyond my ability'
]


# fetching tokens from the text command
def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


def extract_command_from_text(text):
    l = []
    for t in text.split(' '):
        if t.upper() in two_args_operations:
            l.append(t.upper())
        if t.upper() in one_arg_operations:
            l.append(t.upper())
        if t.upper() in no_arg_operations:
            l.append(t.upper())
        if t.upper() in algebraic_operations:
            l.append(t.upper())
    return l


# calculating LCM
def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


# calculating HCF
def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


# Addition
def add(a, b):
    return a + b


# Subtraction
def sub(a, b):
    return a - b


# Multiplication
def mul(a, b):
    return a * b


# Division
def div(a, b):
    return a / b


# Remainder
def mod(a, b):
    return a % b


# Remainder
def square(a):
    return a ** 2

# Cubic
def cubic(a):
    return a ** 3

# Power
def power(a, b):
    return a ** b

# Exponential power
def exp(a):
    return math.e ** a

# Square root
def square_root(a):
    return a ** 0.5

# Cubic root
def cubic_root(a):
    return a ** (1 / 3)

# Root
def root(a, b):
    return a ** (1 / b)

# Natural logarithm
def ln(a):
    return math.log(math.e, a)

# Logarithm
def log(a, b):
    return math.log(a, b)

# Reciprocal
def reciprocal(a):
    return 1 / a

# Sin
def sin(a):
    return math.sin(a)

# Cos
def cos(a):
    return math.sin(a)

# Tan
def tan(a):
    return math.sin(a)

# ArcSin
def asin(a):
    return math.asin(a)

# ArcCos
def acos(a):
    return math.acos(a)

# ArcTan
def atan(a):
    return math.atan(a)

# Randomly generate a value
def rand():
    return random.random()

# Factorial
def factorial(a):
    return math.factorial(a)


# Response to command
# printing - "Thanks for enjoy with me" on exit
def end():
    print(response[2])
    input('press enter key to exit')
    exit()

# get my name
def myname():
    print(response[1])

# print sorry message
def sorry():
    print(response[3])


# Operations - performed on the basis of text tokens

# two arguments operations
two_args_operations = {'ADD': add, 'PLUS': add, 'SUM': add, 'ADDITION': add,
                       'SUB': sub, 'SUBTRACT': sub, 'MINUS': sub,
                       'DIFFERENCE': sub, 'LCM': lcm, 'HCF': hcf,
                       'PRODUCT': mul, 'MULTIPLY': mul, 'MULTIPLICATION': mul,
                       'DIVISION': div, 'MOD': mod, 'REMANDER': mod, 'MODULAS': mod,
                       'POWER': power, 'ROOT': root, 'LOG': log

                       }

# one argument operations
one_arg_operations = {
    'SQUARE': square,
    'CUBIC': cubic,
    'SQUAREROOT': square_root,
    'CUBICROOT': cubic_root,
    'EXP': exp,
    'LN': ln,
    'RECIPROCAL': reciprocal,
    'SIN': sin,
    'COS': cos,
    'TAN': tan,
    'ASIN': asin,
    'ACOS': acos,
    'ATAN': asin,
    'FACTORIAL': factorial,
}

# non arguments operations
no_arg_operations = {
    'RAND': rand,
}

# algebraic operations
algebraic_operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '^': power,
    '%': mod,
}

# commands
commands = {'NAME': myname, 'EXIT': end, 'END': end, 'CLOSE': end}

print('--------------' + response[0] + '------------')
print('--------------' + response[1] + '--------------------')

while True:
    # ask user to input a query str
    print()
    text = input('enter your queries:  ')
    # get parameters from str
    parameters = extract_from_text(text)
    # get commands from str
    cmdlist = extract_command_from_text(text)
    # if there is only one command in query
    if len(cmdlist) == 1:
        # get the command
        cmd = cmdlist[0]
        if cmd in two_args_operations:
            # if it is a two arguments operation
            try:
                func = two_args_operations[cmdlist[0]]
                r = func(parameters[0], parameters[1])
                print(r)
            except:
                print('something went wrong going plz enter again !!')
        elif cmd in one_arg_operations:
            # if it is an one argument operation
            try:
                func = one_arg_operations[cmdlist[0]]
                r = func(parameters[0])
                print(r)
            except:
                print('something went wrong going plz enter again !!')

        elif cmd in no_arg_operations:
            # if it is non arguments operation
            try:
                func = no_arg_operations[cmdlist[0]]
                r = func()
                print(r)
            except:
                print('something went wrong going plz enter again !!')
        elif cmd in algebraic_operations:
            # if cmd is algebraic operation
            try:
                func = algebraic_operations[cmdlist[0]]
                r = func(parameters[0], parameters[1])
                print(r)
            except:
                print('something went wrong going plz enter again !!')
        elif cmd in commands:
            commands[cmd]()
    else:
        # print sorry message
        sorry()
