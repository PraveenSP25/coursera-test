import mysql.connector
mydb=mysql.connector.connect(root='local host',user='root',passwd='Praveen@1998')
mycursor=mydb.mycursor()
mycursor.exicute("show databases")
for i in mycursor:
    print(i)
