# calculator
def add(x, y):
    return x + y

# substract
def substract(x, y):
    return x - y
# multiply
def multiply(x, y):
    return x * y
# divide
def divide(x, y):
    return x / y

keys = ['+', '-', '*', '/']
values = [add, substract, multiply, divide]
operations = {key:value for key, value in zip(keys, values)}

def calculate(x, y, z): 
    function = operations[z]
    answer = function(x, y)
    return answer

#calculate()
num1 = float(input('Whats the first number?: '))
print('  '.join([i for i in operations.keys()]))
operation = input('Pick an operation from above: ') 
num2 = float(input('Whats the next number?: '))
    #calculate()
print(f'{num1} {operation} {num2} = {calculate(num1, num2, operation)}')

data = []
data.append(calculate(num1, num2, operation))

calc = True
while calc == True:
    decision = input('Whant to do another operation? "y" or "n" ')
    if decision == 'n':
        print('Bye!')
        calc = False
    else:
        new_number = float(input('Whats the next number '))
        print('  '.join([i for i in operations.keys()]))
        operation = input('Pick an operation from above: ') 
        new_answer = calculate(new_number, data[-1], operation)
        print(f'{data[-1]} {operation} {new_number} = {new_answer}')
        data.append(new_answer)

