previousNumber = 0
currentNumber = 1

print previousNumber

while currentNumber < 100:
    print currentNumber
    previousNumber, currentNumber = currentNumber, currentNumber + previousNumber
 
