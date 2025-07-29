"""
TODO: put a top level comment here

Author: Gina Lin
Date: 02/04/2024
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply):  T2:45 
"""

def main():
    day = input("\nEnter number of days to report: ")
    
    
    depth = 0
    total = 0


    for i in range(int(day)):
        new_snow = input("\nEnter new snow amount for day " + str(i + 1) + ": ")
        melt_snow = input("Enter amount of snow melt for day " + str(i + 1)+
         ": ")
        depth = float(depth) + float(new_snow) - float(melt_snow)

        print("Snow depth at end of day " + str(i + 1)+ ": " + str(depth))
        
        total = float(total) + float(new_snow)
    
    print("\nTotal snowfall: " + str(total))
       
main()
