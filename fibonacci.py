def fib():
 previousNumber, currentNumber = 0, 1
 print previousNumber,

 while currentNumber < 100:
  print currentNumber,
  previousNumber, currentNumber = currentNumber, currentNumber + previousNumber
 
def fib2(n):
 result = []
 a, b = 0, 1
 while a < n:
  result.append(a)
  a, b = b, a+b
 return result

fib()
print fib2(100)

