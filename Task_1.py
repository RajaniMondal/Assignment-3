n = int(input("Enter the number : "))
def factorial  (n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)
result = factorial(n)
print("Factorial of number", n, "is:", result)