import pymysql
 
db = pymysql.connect("localhost","root","","funread")
 
cursor = db.cursor()
 
cursor.execute("SELECT * from User")
 
# Fetch all the rows in a list of lists.
resultados = cursor.fetchall()
for row in resultados:
    name = row[0]
    print ("ID: ", id, ", nombre: ", name)
 

