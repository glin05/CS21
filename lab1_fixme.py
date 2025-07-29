"""
  This program should first prompt the user for an integer n.

  It should then compute n-squared, i.e. n times n, and store
  the result in a variable called answer. 

  Finally, it should print the value of n and its square.

  Unfortunately, this program has multiple errors.

  Find and fix them all.

  Author: Gina Lin
  Date: 01/28/2025
  Lecture section (delete the two that do not apply): 8:30 9:30 10:30
  Lab section (delete the three that do not apply): T1:05 T2:45 W1:05 W2:45
"""

def main():
    val = input("Enter an integer n: ")
    print(val)

    n = int(val)

    square = n*n

    print(str(n) + (" squared is ")  + str(square))
main()    
