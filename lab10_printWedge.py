"""
Add a top level comment here

Author: Gina Lin
Date: April 15, 2025
Lab section (delete the three that do not apply):T2:45
"""

def main():
    ch = input("Enter a single character: ")
    row = input("How many rows would you like to print?: ")
    n = int(row)
    print_wedge(ch, n)

def print_wedge(ch, n):
    """
    Prints a wedge using the symbol ch with height of n.
    You can assume n is greater than or equal to zero.

    Parameters:
        n (int): an integer n>=0 representing the number of rows to print
        ch (str): a single character string to use for the tower

    Returns:
        None

    Side effects:
        Prints a wedge of n rows using the character ch.
   """
    if n == 0:
        print('')
    if n > 0:
        print(ch * n)
        print_wedge(ch, n-1)

if __name__ == '__main__':
    main()
