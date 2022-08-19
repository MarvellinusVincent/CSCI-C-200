import sqlite3
import os


# Basic starter code is given below

# Initialize a connection
connection = sqlite3.connect("mydatabase.db")

# Get the cursor to the connection
my_cursor = connection.cursor()
my_cursor.execute("DROP TABLE IF EXISTS Weather")
my_cursor.execute("CREATE TABLE Weather (City text, State text, High number, Low number)")
my_cursor.execute("INSERT INTO Weather VALUES('Phoenix', 'Arizona', 105, 90)")
my_cursor.execute("INSERT INTO Weather VALUES('Tucson', 'Arizona', 101, 92)")
my_cursor.execute("INSERT INTO Weather VALUES('Flag Staff', 'Arizona', 105, 90)")
my_cursor.execute("INSERT INTO Weather VALUES('San Diego', 'California', 77, 60)")
my_cursor.execute("INSERT INTO Weather VALUES('Albuquerqu', 'New Mexico', 80, 72)")
my_cursor.execute("INSERT INTO Weather VALUES('Nome', 'Alaska', 64, -54)")
# TODO: Create Table and Insert Values (use the below data to populate the table)

data = [
    ('Phoenix', 'Arizona', 105, 90),('Tucson', 'Arizona', 101, 92),
    ('Flag Staff', 'Arizona', 105, 90), ('San Diego', 'California', 77, 60),
    ('Albuquerque', 'New Mexico', 80, 72), ('Nome', 'Alaska', 64 ,-54)
]

if __name__=="__main__":

    # QUERY 1 Select all the tuples
    print ()
    print ("*" * 40)
    print ("Problem 3")
    print ()
    print("Query 1")
    for i in my_cursor.execute("SELECT * FROM Weather"):
        print(i)
    print("List Comprehension: ", data)


    # QUERY 2 
    # Select All the tuples where the high temperature is less than 80
    print ("*" * 30)
    print("\nQuery 2")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT * FROM Weather where High <80"):
        print (i)
    print("List Comprehension: ", [d for d in data if d[2] < 80 ])


    # QUERY 3 
    # Select All the cities where the low temperature is greater than the low of Albuquerque 
    print ("*" * 30)
    print("\nQuery 3")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT City FROM Weather where Low > (SELECT Low FROM Weather WHERE City == 'Albuquerqu')"):
        print (i)
    print("List Comprehension: ",[d[0] for d in data if d[3] > [d[3] for d in data if d[0] == 'Albuquerque'][0]])


    # QUERY 4 
    # Select the city and temperature with the smallest low temperature 
    print ("*" * 30)
    print("\nQuery 4")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT City, MIN(Low) FROM Weather"):
        print (i)
    print("List Comprehension: ",[(d[0],d[3]) for d in data if d[3] in (sorted(data, key = lambda x:x[3])[0])])


    # QUERY 5 
    # Select the city temperature with the largest high temperature 
    print ("*" * 30)
    print("\nQuery 5")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT City, High FROM Weather WHERE High == (SELECT MAX(High) FROM Weather)"):
        print (i)
    print("List Comprehension: ",[(d[0],d[2]) for d in data if d[2] in (sorted(data, key = lambda x:x[2],reverse=True)[0])])


    # QUERY 6 
    # Display the average High and Low temperatures
    # You are not allowed to use Avg()
    print ("*" * 30)
    print("\nQuery 6")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT CAST(SUM(High) AS REAL) / COUNT (*), CAST(SUM(Low) AS REAL) / COUNT (*) FROM Weather"):
        print (i)
    print("List Comprehension: ", [(sum([d[2] for d in data])/len(data),sum([d[3] for d in data])/len(data))])


    # QUERY 7 
    # Give the counts of cities by their Low temperatures
    print ("*" * 30)
    print("\nQuery 7")
    # TODO: Put query here
    for i in my_cursor.execute("SELECT Low, COUNT(*) FROM Weather GROUP BY Low HAVING Low IN (SELECT DISTINCT Low FROM Weather)"):
        print (i)
    print("List Comprehension: ", [(i,list(map((lambda x: x[3]),data)).count(i)) for i in set(map((lambda x: x[3]),data))])

connection.close()
