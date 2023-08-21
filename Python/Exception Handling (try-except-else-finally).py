try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    result = "Error: Division by zero"
except ValueError:
    result = "Error: Invalid input"
else:
    result = "Result: " + str(result)
finally:
    print(result)
