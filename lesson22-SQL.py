import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server}:'
                              'Server=Manowabe\SQLExpress;'
                              'Database = northwind;'
                              'uid=username;'
                              'pwd=mypasswpd;')


cursor = connection.cursor()

mysqlquery = ("""
                SELECT CompanyName, ContactName, country
                FROM dbo.Customres
                WHERE Country='Canada'
              """)


cursor.execute(mysqlquery)

results = cursor.fetchall()
print(results)


for row in results:
     CompanyName = row[0]
     ContactName = row[1]
     country = row[2]

     print("welcome company" + str(CompanyName) + 'user' + str(ContactName) + str(country))
connection.close()