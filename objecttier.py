#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through
# the data tier.
#
# Original author: Ellen Kidane
#
#   Student: Divya Shah, dshah86, 655844407
#   Program 2: Chicago Lobbyist Database App
#   Course: CS 341, Spring 2024
#   System: MacOS using PyCharm with SQL
#   References: https://www.alibabacloud.com/blog/how-to-write-a-high-performance-sql-join-implementation-and-best-practices-of-joins_599145,
#   https://medium.com/analytics-vidhya/introduction-to-sql-using-python-using-join-statements-to-merge-multiple-tables-3b3513fe2c98
#   https://www.youtube.com/watch?v=Vy8NRI24aXg
import datatier

##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID
    @property
    def First_Name(self):
        return self._First_Name
    @property
    def Last_Name(self):
        return self._Last_Name
    @property
    def Phone(self):
        return self._Phone

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City,
                 State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
        self._Lobbyist_ID = Lobbyist_ID
        self._Salutation = Salutation
        self._First_Name = First_Name
        self._Middle_Initial = Middle_Initial
        self._Last_Name = Last_Name
        self._Suffix = Suffix
        self._Address_1 = Address_1
        self._Address_2 = Address_2
        self._City = City
        self._State_Initial = State_Initial
        self._Zip_Code = Zip_Code
        self._Country = Country
        self._Email = Email
        self._Phone = Phone
        self._Fax = Fax
        self._Years_Registered = Years_Registered
        self._Employers = Employers
        self._Total_Compensation = Total_Compensation
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID
    @property
    def Salutation(self):
        return self._Salutation
    @property
    def First_Name(self):
        return self._First_Name
    @property
    def Middle_Initial(self):
        return self._Middle_Initial
    @property
    def Last_Name(self):
        return self._Last_Name
    @property
    def Suffix(self):
        return self._Suffix
    @property
    def Address_1(self):
        return self._Address_1
    @property
    def Address_2(self):
        return self._Address_2
    @property
    def City(self):
        return self._City
    @property
    def State_Initial(self):
        return self._State_Initial
    @property
    def Zip_Code(self):
        return self._Zip_Code
    @property
    def Country(self):
        return self._Country
    @property
    def Email(self):
        return self._Email
    @property
    def Phone(self):
        return self._Phone
    @property
    def Fax(self):
        return self._Fax
    @property
    def Years_Registered(self):
        return self._Years_Registered
    @property
    def Employers(self):
        return self._Employers
    @property
    def Total_Compensation(self):
        return self._Total_Compensation

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone
        self._Total_Compensation = Total_Compensation
        self._Clients = Clients
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID
    @property
    def First_Name(self):
        return self._First_Name
    @property
    def Last_Name(self):
        return self._Last_Name
    @property
    def Phone(self):
        return self._Phone
    @property
    def Total_Compensation(self):
        return self._Total_Compensation
    @property
    def Clients(self):
        return self._Clients
##################################################################
#
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
    sql = "SELECT COUNT(*) FROM LobbyistInfo;"
    lobbyist = datatier.select_one_row(dbConn, sql)
    if lobbyist is not None:
        return lobbyist[0]
    else:
        return -1

##################################################################
#
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
    sql = "SELECT COUNT(*) FROM EmployerInfo;"
    employers = datatier.select_one_row(dbConn, sql)
    if employers is not None:
        return employers[0]
    else:
        return -1

##################################################################
#
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
    sql = "SELECT COUNT(*) FROM ClientInfo;"
    clients = datatier.select_one_row(dbConn, sql)
    if clients is not None:
        return clients[0]
    else:
        return -1

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and %
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID;
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
    checkPattern = [pattern, pattern]
    sql = """SELECT Lobbyist_ID, First_Name, Last_Name, Phone 
            FROM LobbyistInfo 
            WHERE First_Name LIKE ? OR Last_Name LIKE ? 
            ORDER BY Lobbyist_ID;
    """
    lobbyists = datatier.select_n_rows(dbConn, sql, checkPattern)
    lobby = []
    for row in lobbyists:
        lobby.append(Lobbyist(row[0], row[1], row[2], row[3]))
    return lobby

##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    sql = """SELECT LobbyistInfo.Lobbyist_ID, LobbyistInfo.Salutation, LobbyistInfo.First_Name, LobbyistInfo.Middle_Initial, 
            LobbyistInfo.Last_Name, LobbyistInfo.Suffix, LobbyistInfo.Address_1, LobbyistInfo.Address_2, LobbyistInfo.City, 
            LobbyistInfo.State_Initial, LobbyistInfo.ZipCode, LobbyistInfo.Country, LobbyistInfo.Email, LobbyistInfo.Phone, LobbyistInfo.Fax,
            SUM(Compensation.Compensation_Amount) AS total
            FROM LobbyistInfo
            LEFT JOIN Compensation ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
            WHERE LobbyistInfo.Lobbyist_ID = ?
            GROUP BY LobbyistInfo.Lobbyist_ID;
    """
    lobbyComp = datatier.select_one_row(dbConn, sql, [lobbyist_id])
    if not lobbyComp:
        return None
    total = lobbyComp[15] if lobbyComp[15] is not None else 0.0

    sql2 = """SELECT DISTINCT Year
            FROM LobbyistYears 
            Where Lobbyist_ID = ?;
    """
    yearResult = datatier.select_n_rows(dbConn, sql2, [lobbyist_id])
    yearsSql = [row[0] for row in yearResult]

    sql3 = """SELECT DISTINCT Employer_Name
            FROM EmployerInfo 
            INNER JOIN LobbyistAndEmployer ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
            WHERE LobbyistAndEmployer.Lobbyist_ID = ?
            ORDER BY Employer_Name ASC;
    """
    employerResult = datatier.select_n_rows(dbConn, sql3, [lobbyist_id])
    employee = [row[0] for row in employerResult]

    return LobbyistDetails(lobbyComp[0], lobbyComp[1], lobbyComp[2], lobbyComp[3], lobbyComp[4], lobbyComp[5], lobbyComp[6], lobbyComp[7],
            lobbyComp[8], lobbyComp[9], lobbyComp[10], lobbyComp[11], lobbyComp[12], lobbyComp[13], lobbyComp[14], yearsSql, employee, total)

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid.
#          An empty list is also returned if an internal error
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
    sql = """SELECT LobbyistInfo.Lobbyist_ID, LobbyistInfo.First_Name, LobbyistInfo.Last_Name, LobbyistInfo.Phone, SUM(Compensation.Compensation_Amount) AS total
            FROM LobbyistInfo
            Inner JOIN Compensation ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
            WHERE strftime('%Y', Compensation.Period_Start) <= ? AND strftime('%Y', Compensation.Period_End) >= ?
            GROUP BY LobbyistInfo.Lobbyist_ID
            ORDER BY total DESC
            LIMIT ?;
    """
    lobbyistsResult = datatier.select_n_rows(dbConn, sql, [year, year, N])
    lobbyist = []
    if lobbyistsResult:
        for row in lobbyistsResult:
            sql2 = """SELECT Distinct ClientInfo.Client_Name, ClientInfo.Client_ID
                    FROM ClientInfo
                    INNER JOIN Compensation ON ClientInfo.Client_ID = Compensation.Client_ID
                    WHERE Compensation.Lobbyist_ID = ? 
                    AND strftime('%Y', Compensation.Period_Start) <= ? AND strftime('%Y', Compensation.Period_End) >= ?
                    ORDER BY ClientInfo.Client_Name;
            """
            clients = [clientRow[0] for clientRow in datatier.select_n_rows(dbConn, sql2, [row[0], year, year])]
            lobbyist.append(LobbyistClients(row[0], row[1], row[2], row[3], row[4], clients))
    return lobbyist

##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below),
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    sql = "SELECT * FROM LobbyistYears WHERE Lobbyist_ID = ?;"
    lobbyist = datatier.select_one_row(dbConn, sql, [lobbyist_id])

    if lobbyist and lobbyist[0] != 0:
        sqlInsert = "INSERT INTO LobbyistYears (Lobbyist_ID, Year) VALUES (?, ?);"
        result = datatier.perform_action(dbConn, sqlInsert, [lobbyist_id, year])
        if result:
            return 1
        else:
            return 0
    else:
        return 0

##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
    sql = "UPDATE LobbyistInfo SET Salutation = ? WHERE Lobbyist_ID = ?;"
    lobbyist = datatier.perform_action(dbConn, sql, [salutation, lobbyist_id])
    if lobbyist:
        return 1
    else:
        return 0
