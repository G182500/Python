import mysql.connector
import uuid
from datetime import datetime

def salvarBanco(nome_pdf, values, status):
    cnx = mysql.connector.connect(user='b09a83c4724f0a', 
                                    password='5968583e',
                                    host='us-cdbr-east-06.cleardb.net', 
                                    database='heroku_2409cf2cf4dd08d', 
                                    charset="utf8")
    #cnx = mysql.connector.connect(user='root', password='synvia@123',host='localhost', database='localrobogq')

    try:
        cursor = cnx.cursor()

        sql = "INSERT INTO logrobogqs(Id, Data, nomePDF, LOG, status) VALUES(%s, %s, %s, %s, %s)" 
        valores = (str(uuid.uuid4()), datetime.today(), nome_pdf, values, status)

        cursor.execute(sql, valores)
        cnx.commit()
        print('Salvo com sucesso no banco de dados')

    finally:
        cnx.close()