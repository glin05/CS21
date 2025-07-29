"""
Add a top level comment here

Author: Gina Lin
Date: April 15, 2025
Lab section (delete the three that do not apply):T2:45
"""

def main():
    base = int(input("Enter a base numer: "))
    n = int(input("How many multiples would you like to display? "))
    mult = get_multiples(base, n)
    print(mult)

def get_multiples(base, n):
   """
    This function creates a list of length n containing the first n
    multiples of the base number.

    Parameters:
       base (int): a number to create multiples from
       n (int): the desired number of multiples

    Returns:
       (list): a list of the first n multiples of the base number
    """

   if n == 0: 
      return []
   part = get_multiples(base, n - 1)
   if n > 0: 
      ans = part + [base * n]
      return ans 
        
if __name__ == '__main__':
    main()
