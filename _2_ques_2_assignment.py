
"""Write a Python program to print a dictionary whose keys 
should be the alphabet from a-z and the value should be corresponding ASCII values"""

str = input("Enter a string: ")
print("Output : ")
for ch in str:
    ascii = ord(ch)
    dict = {ch:ascii}
    print(dict, end = " ")


