import mysql.connector

mydb = mysql.connector.connect(
    host="*********",
    user="*********",
    password="*********",
    database="*********",
    
)

mycursor = mydb.cursor()

mycursor.execute("SELECT id FROM producto")

ids = mycursor.fetchall()

mycursor.execute("SELECT foto FROM producto")
fotos = mycursor.fetchall()

for x in range(0,len(ids)):
    foto = str(fotos[x])[3:18]
    mycursor.execute("""INSERT INTO imagen (id,producto_id,nombre) VALUES (%s,%s,%s)""",[x+1,x+1,foto])
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


