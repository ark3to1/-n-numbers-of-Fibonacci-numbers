n = int(input("Enter the till the number of Fibonacci numbers to be printed: "))
print(f"\nFibonacci Numbers till {n} are: ", end="")

a, b = 0, 1
print(b, end=' ')

while b <= n:
    a, b = b, a + b
    if b <= n:
      print(b, end=' ')