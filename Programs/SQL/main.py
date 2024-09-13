import mysql.connector as mysql

database="raydb"
conn = mysql.connect(host="localhost", user="root", password="root", database="raydb")
print(conn.is_connected()*f"Connection established to {database}" or f"Access denied to {database}")

cursor = conn.cursor()
cursor.execute("SELECT * FROM Student;")
data = cursor.fetchmany(3)

print(data)