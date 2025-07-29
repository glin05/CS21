"""
This program reads a data set of earthquake statistics that contain
a unique ID, magintude, location, longitude and latitude, and 
the date and time of each earthquake. Then then program prompts the user
to search by location, ID, or magnitude; and also provides a Quit option. 
Functions perform input validation and then uses linear or binary search 
based on which option is chosen. 

Authors: Gina Lin
Date: 04/01/2025
Lab section (delete the three that do not apply): T2:45
Lecture section: 8:30
"""

from earthquakes_lab import *

def main():
    data = open_file()
    search = True 
    while search:
        selection = menu()
        resp = more_info(selection, data) 
        if resp != 123: 
            display = output(resp)
        else:
            search = False
        
def open_file():
    """
    Reads the given file and returns a list of earthquake objects.
    
    Parameter:
    none
    
    Returns:
    data (list): list of earthquake objects.
    """
    fp = open("/usr/local/doc/earthquakes.txt", 'r')
    data = []
    for line in fp:
        line = line.strip()
        info = line.split(";")
        
        ID = info[0]
        mag = float(info[1])
        loc = info[2]
        lat = float(info[3])
        longt = float(info[4])
        s_loc = info[5]
        time = info[6]

        stats = Earthquake(ID,mag,loc,lat,longt,s_loc,time)
        data.append(stats)
    fp.close()
    return data

def menu():
    """
    Performs input validation that continuosly prompts user 
    for correct menu option and returns user input to main if input valid.
    
    Parameters: none

    Returns:
    selection(str): user input from menu options
    """
    print(" ")
    print("Please select one of the following choices:")
    print("(1) Find by location")
    print("(2) Find by ID")
    print("(3) Find by magnitude")
    print("(4) Quit")
    print("")
    selection = input("Choice? ")
    not_valid = True
    while not_valid:
        if not selection.isdigit() or int(selection) < 1 or int(selection)> 4:  
            print("Choice is not valid") 
            selection = input("Choice? ")
        else:
            return selection
            not_valid = False
            
def more_info(selection, data): 
    """
    Based on user's selection from menu, this function will prompt
    them to provide more information to search dataset by location,
    ID, minimum and maximum magnitudes, or exit the program.
    
    Parameters:
    selection(str): user input from menu options
    data (list): list of earthquake objects.
   
    Returns:
    selc_loc (lst): user location search results
    selc_id (str) : user id search results
    selc_mag (str): user magnitude search results
    """
    
    if int(selection) == 1:
        enter_loc = input("Enter location: ")
        loc_cap = enter_loc.capitalize()
        selc_loc = search_loc(loc_cap, data)
        if len(selc_loc) == 0:
            print("No records match entered location.")
        return selc_loc

    if int(selection) == 2:
        enter_id = input("Enter ID: ")
        selc_id = search_id(enter_id, data)
        return selc_id 
        
    if int(selection) == 3:
        is_mag = False 
        while is_mag == False:
            minm = input("Enter minimum magnitude: ")
            if is_float(minm) == False: 
                print("Invalid input. Please try again")
            if is_float(minm) == True:
                is_mag = True
        is_magmax = False 

        while is_magmax == False:
            maxm = input("Enter maximum magnitude: ")
            if is_float(maxm) == False or float(maxm) <= float(minm): 
                print("Invalid input. Please try again")
            elif is_float(maxm) == True:
                is_magmax = True
        selc_mag = search_mag(minm, maxm, data) 
        return selc_mag

    if int(selection) == 4:
        print("Goodbye!")
        return 123

def search_loc(loc_cap, data):
    """
    This function uses linear search to search for locations that match 
    loc_cap and data. 

    Parameters:
        loc_cap(str): user inputed location 
        data (list): list of earthquake objects
    
    Returns: 
        loc_lst(list): search results based loc_cap
    """
    loc_lst = []
    for i in range(len(data)):
        new_data = data[i].get_location_full()
        if loc_cap in new_data:
            loc_lst.append(data[i])
    return loc_lst
   
def search_id(enter_id, data):
    """
    This function uses binary search to search for ID's that match 
    enter_id and data. Notifies user if ID wasn't found.

    Parameters:
        enter_id(string): user inputed eqarthquate ID
        data (list): list of earthquake objects.

    Returns:
        result(str): search results based on enter_id or if not found
        
    """
    lo = 0
    hi = len(data)-1
    while  lo <= hi :
     mid = (lo + hi) // 2
     if data[mid].get_id() == enter_id:
         return [data[mid]]
     elif data[mid].get_id() > enter_id:
         hi = mid -1
     else:
         lo = mid + 1
    return []

def search_mag(minm, maxm, data):
    """
    This function ensures that a valid float for magnitudes are entered and will keep 
    prompting until valid responses are entered. 
    
    Parameters:
        minm(float): user inputed minimum magnitude
        maxm(float): user inputed minimum magnitude
        data(list): list of earthquake objects.

    Returns:
        result(float): search results based on minm and maxm
    """  
    mag_lst = []

    for i in range(len(data)):
        mag_data = data[i].get_magnitude()
        if float(minm) <= mag_data and float(maxm) >= mag_data:
            mag_lst.append(data[i])
    return mag_lst

    action = print("Invalid input. Please try again.")
    return action

def output(resp):
    """
    Prints list of earthquake search results

    Parameters:
        resp(lst): are the earthquake search results 
   
    Returns: None
    """
    print("")
    print("Found " + str(len(resp)) + " results:")
    for i in resp:
        print(i)

main()
