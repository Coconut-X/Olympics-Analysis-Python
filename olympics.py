# import mysql.connector 
# import numpy as np
# import matplotlib.pyplot as plt


# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="culmination@2",
#     database="olympics"
# )

# print("Starting to print years...")

# mycursor = mydb.cursor()

# years=np.array([],dtype=int)
# males=np.array([],dtype=int)
# females=np.array([],dtype=int)

    
# # Query for years
# mycursor.execute("select distinct Year from athletes")
# result = mycursor.fetchall()

# years = np.array([], dtype=int)

# for row in result:
#     years = np.append(years, row[0])

# males = np.array([], dtype=int)
# females = np.array([], dtype=int)
# meanAge=np.array([],dtype=float)


# y = int(0)

# while y < len(years): 
#     # Query for male athletes
#     m = "select count(*) from athletes where Year=%s and Sex='M'"
#     mycursor.execute(m, (int(years[y]),))
#     result = mycursor.fetchone()
#     males = np.append(males, result[0])

#     # Query for female athletes
#     f = "select count(*) from athletes where Year=%s and Sex='F'"
#     mycursor.execute(f, (int(years[y]),))
#     result = mycursor.fetchone()
#     females = np.append(females, result[0])
    
#     y += 1
    
# # Ensure the arrays are sorted by year, argsort returns the indices that would sort the array
# sorted_indices = np.argsort(years)
# years_sorted = years[sorted_indices]
# males_sorted = males[sorted_indices]
# females_sorted = females[sorted_indices]

# # Plot the sorted data
# plt.subplot(2,1,1)
# plt.plot(years_sorted, males_sorted, label='Males', marker = 'o')
# plt.plot(years_sorted, females_sorted, label='Females', marker = 'o')
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.title('Male and Female Participation in Olympics Over the Years')
# plt.legend()


# #================================================================================================

# #Showing top 12 teams by gold medals

# mycursor.execute("""
#     SELECT Team, COUNT(*) AS gold_medals
#     FROM athletes
#     WHERE Medal = 'Gold'
#     GROUP BY Team
#     ORDER BY gold_medals DESC
#     LIMIT 12;
# """)
# result = mycursor.fetchall()


# teams = []
# gold_medals = []

# for row in result:
#     teams.append(row[0]) 
#     gold_medals.append(row[1])


# teams = np.array(teams)
# gold_medals = np.array(gold_medals)

# # Plotting the data
# plt.subplot(2,1,2)
# plt.barh(teams, gold_medals, color='gold')
# plt.xlabel('Number of Gold Medals')
# plt.ylabel('Teams')
# plt.title('Top 12 Teams by Gold Medals')
# plt.gca().invert_yaxis()  # To display the highest value at the top
# plt.tight_layout() 
# plt.show()


import mysql.connector
import csv

# Step 1: Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="culmination@2",
    database="olympics"
)

mycursor = mydb.cursor()

# Step 2: Execute query to select all data from the athletes table
mycursor.execute("SELECT * FROM athletes")

# Fetch all rows from the table
rows = mycursor.fetchall()

# Step 3: Get column names
column_names = [i[0] for i in mycursor.description]

# Step 4: Open a new CSV file and write the data
with open('athletes.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the column headers
    csvwriter.writerow(column_names)
    
    # Write the rows from the table
    csvwriter.writerows(rows)

print("Data exported successfully to athletes.csv")

# Close the cursor and the database connection
mycursor.close()
mydb.close()
