#var number1,operator,number2:entier
import math
number1 = float(input('Number 1 :'))
operator = input('operator (*, /, +, -, ^, mod, div, sqrt(squar root)):')
number2 = float(input('Number 2 :'))
if(operator == '+'):
    result = float(number1 + number2)
    
elif(operator == '-'):
    result = float(number1 - number2)
    
elif(operator == '*'):
    result = float(number1 * number2)
    
elif(operator == '/')and (number2>0) and (number2<0):
    result = float(number1 / number2)

elif(operator == '/')and (number2 == 0):
    result = ('Math domain Eroor, Number 2 can\'t equal 0')
    
elif(operator == 'div'):
    result = float(number1 // number2)
    
elif(operator == 'mod'):
    result = float(number1 % number2)
    
elif(operator == '^'):
    result = float(number1 ** number2)
    
elif(operator == 'sqrt') and (number2 >= 0):
    result = float(number1 * math.sqrt(number2))
    
elif(operator == 'sqrt') and (number2 < 0):
    result = ('Math domain Eroor, Number 2 is Not greater than or equal to 0')
else:
    result = ('use a Operator form this: *, /, +, -, ^, %, // or sqrt(squar root) ')
    
print(result)