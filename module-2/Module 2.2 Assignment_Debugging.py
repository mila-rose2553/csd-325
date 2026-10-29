#Mariana Baker, Module 2.2 Assignment, 10/29/26
#Program to capture the debugging activity
def get_factorial(n):
    """Return the factorial of a non-negative integer."""
    if n < 0:
        return "Error: n must be a non-negative integer"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print("Factorial:", get_factorial(num))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
