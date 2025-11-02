#Write a Python program that takes any word as an input from the user and then creates a function that accepts the same word as a parameter and checks whether it is a palindrome or not. (Palindrome word is the same when read in both directions - forward or backward. Example - racecar)
a=input("Enter a word ")

def palindrome(word):
    print("Checking if the word is palindrome or not")
    reverse=word[::-1]
    if word==reverse:
        print("Its a palindrome")
    else:
        print("Its not a palindrome")    

    

palindrome(a)    