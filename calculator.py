import argparse

def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    return x / y

# Create a parser object
parser = argparse.ArgumentParser(description='Simple Calculator')

# Add arguments to the parser
parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'],
                    help='Mathematical operation to perform')
parser.add_argument('operand1', type=float, help='First operand')
parser.add_argument('operand2', type=float, help='Second operand')

# Parse the arguments
args = parser.parse_args()

# Perform the specified operation
result = None

if args.operation == 'add':
    result = add_numbers(args.operand1, args.operand2)
elif args.operation == 'subtract':
    result = subtract_numbers(args.operand1, args.operand2)
elif args.operation == 'multiply':
    result = multiply_numbers(args.operand1, args.operand2)
elif args.operation == 'divide':
    result = divide_numbers(args.operand1, args.operand2)

# Print the result
print(f'Result: {result}')
