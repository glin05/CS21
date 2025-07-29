"""

TODO: This porgram uses operators to perfom mathematical functions

Author: Gina Lin
Date: 01/28/2025
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply): T2:45 
"""

def main(): 
    num = input("Enter the first positive integer value: ")
    print(num)
    num2 = input( "Enter the second positive integer value: ")
    print(num2)
    mult = int(num) * int(num2)
    print(str(num) + " * " + str(num2) + " = " + str(mult))
    div = int(num) / int(num2)
    print(str(num) + " / " + str(num2) + " = " + str(div))
    whole = int(num) // int(num2)
    print(str(num) + " // " + str(num2) + " = " + str(whole))
    add = int(num) + int(num2)
    print(str(num) + " + " + str(num2) + " = " + str(add))
    sub = int(num) - int(num2)
    print(str(num) + " - " + str(num2) + " = " + str(sub))
main()
