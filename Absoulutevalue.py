#Write a Python program that will take a number as an input from the user and then creates a function that accepts the same number as a parameter and returns its absolute value. (Example - a negative number is converted to a positive number, the positive number remains the same)
num=int(input("Enter a number"))
def number(a):
    if a<0:
        return -a
    else:
        return a
result=number(num)
print(result)

