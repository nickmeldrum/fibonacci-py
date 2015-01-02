previousNumber = 0
currentNumber = 1

print previousNumber
print currentNumber

while currentNumber < 100:
    nextNumber = currentNumber + previousNumber
    print nextNumber
    previousNumber = currentNumber
    currentNumber = nextNumber
