def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)


#This code calculates the factorial of a number using a recursive function.