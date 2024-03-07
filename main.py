#   Student: Divya Shah, dshah86, 655844407
#   Program 2: Chicago Lobbyist Database App
#   Course: CS 341, Spring 2024
#   System: MacOS using PyCharm with SQL
#   References: In - class PDF's.

import sqlite3
import objecttier


# Below our the 6 helper fucntions for each command + the gernal function, each fucntion has their own outputs and error handling.
def geernalStats(dbConn):
    num_lobbyists = objecttier.num_lobbyists(dbConn)
    num_employers = objecttier.num_employers(dbConn)
    num_clients = objecttier.num_clients(dbConn)

    print("** Welcome to the Chicago Lobbyist Database Application **")
    print("General Statistics:")
    print(f" Number of Lobbyists: {num_lobbyists:,}")
    print(f" Number of Employers: {num_employers:,}")
    print(f" Number of Clients: {num_clients:,}")


# This fucntion just prints the general stats at the begining when the program is first run.
# It calls the num_lobbyists and num_employers and num_client fucntions from the object tier file.
def commandOne(dbConn):
    print()
    name = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
    print()
    results = objecttier.get_lobbyists(dbConn, name)
    lobbyists = len(results)
    print(f"Number of lobbyists found: {lobbyists}")
    print()
    if lobbyists > 100:
        print("There are too many lobbyists to display, please narrow your search and try again...")
    else:
        for row in results:
            print(f"{row.Lobbyist_ID} : {row.First_Name} {row.Last_Name} Phone: {row.Phone}")


# This fucntion asks the user for a name and prints out all the lobbyists that match that name, first or last.
# It prints out the first name, last name and phone number, it calls the get_lobbyists funciton from object tier.
def commandTwo(dbConn):
    print()
    while True:
        lobbyist = input("Enter Lobbyist ID: ")
        print()
        if not lobbyist.isdigit():
            print("Invalid input. Lobbyist ID must be a number.")
            print()
            continue

        lobbyist = int(lobbyist)
        results = objecttier.get_lobbyist_details(dbConn, lobbyist)
        if results:
            print(f"{results.Lobbyist_ID} :")
            print(f" Full Name: {''.join([results.Salutation + ' ' if results.Salutation else '', results.First_Name, ' ', results.Middle_Initial, ' ', results.Last_Name, ' ', results.Suffix])}")
            print(f" Address: {results.Address_1} {results.Address_2} , {results.City} , {results.State_Initial} {results.Zip_Code} {results.Country}")
            print(f" Email: {results.Email}")
            print(f" Phone: {results.Phone}")
            print(f" Fax: {results.Fax if results.Fax else ''}")
            years = ', '.join(map(str, results.Years_Registered))
            print(f" Years Registered: {years}, ")
            employers = ', '.join(results.Employers)
            print(f" Employers: {employers}, ")
            print(f" Total Compensation: ${results.Total_Compensation:,.2f}")
            break
        else:
            print("No lobbyist with that ID was found.")
            break


# This fucntion asks the user for the year and how many top lobbyist they would like to see and prints out there information
# This fucntion calls on the get_top_N_lobbyists function from object tier to get all the nessary information
def commandThree(dbConn):
    print()
    NVal = input("Enter the value of N: ")

    if not NVal.isdigit() or int(NVal) <= 0:
        print("Please enter a positive value for N...")
        print()
        return

    year = input("Enter the year: ")

    lobbyists = objecttier.get_top_N_lobbyists(dbConn, int(NVal), year)

    if not lobbyists:
        print()
    else:
        print()
        for idx, lobbyist in enumerate(lobbyists, start=1):
            print(f"{idx} . {lobbyist.First_Name} {lobbyist.Last_Name}")
            print(f"  Phone: {lobbyist.Phone}")
            print(f"  Total Compensation: ${lobbyist.Total_Compensation:,.2f}")
            print("  Clients:", ", ".join(lobbyist.Clients) + ", ")


# This function registers an exisitng lobbyist for a new year by asking the user for a year and a lobbyist ID
# This fucntion calls on the add_lobbyist_year funciton from object tier.
def commandFour(dbConn):
    print()
    year = input("Enter year: ")
    lobbyist = input("Enter the lobbyist ID: ")
    result = objecttier.add_lobbyist_year(dbConn, lobbyist, year)

    if result > 0:
        print()
        print("Lobbyist successfully registered.")
    else:
        print()
        print("No lobbyist with that ID was found.")
    print()

# This fucntion sets the salutation for a inputed lobbyist based on ID, the user has the option of what pre-fix for what lobbyist
# This fuction uses the get_lobbyist_details and set_salutation fucntiosn from object tier.
def commandFive(dbConn):
    print()
    lobbyistID = input("Enter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")
    print()
    result = objecttier.get_lobbyist_details(dbConn, lobbyistID)

    if result is not None:
        setName = objecttier.set_salutation(dbConn, lobbyistID, salutation)
        if setName:
            print("Salutation successfully set.")
        else:
            print("Failed to set salutation.")
    else:
        print("No lobbyist with that ID was found.")



# MAIN Function - connects to database and controls the loop depening on user command.
dbConn = sqlite3.connect("Chicago_Lobbyists.db")
geernalStats(dbConn)
print()
# Command loop
while True:
    command = input("Please enter a command (1-5, x to exit): ")
    if command == 'x':
        dbConn.close()
        break
    elif command == '1':
        commandOne(dbConn)
    elif command == '2':
        commandTwo(dbConn)
    elif command == '3':
        commandThree(dbConn)
    elif command == '4':
        commandFour(dbConn)
    elif command == '5':
        commandFive(dbConn)
    else:
        print("**Error, unknown command, try again...")
    print()
