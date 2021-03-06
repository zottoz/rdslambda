import json
import pymysql


RDS_endpoint = "my-db-1.c1tumcbllwas.us-east-1.rds.amazonaws.com"
UserName = "admin"
Password = "admin123"
DatabaseName = "dados"

connectionString = pymysql.connect(RDS_endpoint, user= UserName, passwd= Password, db= DatabaseName)

def lambda_handler(event, context):
    header = []
    row_json = []
    table_json = {}
    connectionString = pymysql.connect(RDS_endpoint, user= UserName, passwd= Password, db= DatabaseName)
    pointer = connectionString.cursor()
    pointer2 = connectionString.cursor()
    pointer.execute('SELECT * FROM alunos')
    
    pointer2.execute('DESCRIBE alunos')
    #print(pointer2.fetchall())
    
    table_head = pointer2.fetchall()
    for head in table_head:
        header.append(head[0])
    #print(header)
    
    table_rows = pointer.fetchall()
    #print(table_rows)
    
    for r in table_rows:
        row_json.append({header[0] : r[0], header[1] : r[1], header[2] : r[2]})
    table_json = {"alunos" : row_json}
    for r in table_rows:
        print("---------------------------------")
        print("ID : {}".format(r[0]))
        print("Nome : {}".format(r[1]))
        print("Matricula : {}".format(r[2]))
        print("---------------------------------")
    
    return table_json