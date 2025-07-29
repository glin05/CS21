"""
This program asks the user to input a word and counts the total 
number of vowels regardless of case.

Author: Gina Lin
Date: April 15, 2025
Lab section (delete the three that do not apply):T2:45
"""

def main():
    resp = input("Enter text: ")
    text = resp.upper()
    num = count_vowels(text)
    print("Number of vowels: %d" % (num))

def count_vowels(text):
    """
    This function counts the number of vowels in the give text.
    The vowels include a, e, i, o, and u. It should count the vowels
    regardless of their case.

    Parameters:
        text (str): a string of text

    Returns:
        int: the number of vowels in the text
    """
    vowels = ["A", "E", "I", "O", "U"]
    if text == "":
        return 0
    rest = text[1:]
    part = count_vowels(rest)
    ans = part
    if text[0] in vowels:
        ans = ans + 1

    return ans

if __name__ == '__main__':
    main()
