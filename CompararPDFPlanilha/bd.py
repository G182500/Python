import mysql.connector
import uuid
from datetime import datetime

def salvarBanco(nome_pdf, values, status):
    cnx = mysql.connector.connect(user='xxxxxx', 
                                    password='yyyyyyy',
                                    host='sdsdsdsdsds', 
                                    database='blablabla', 
                                    charset="utf8")
    
    try:
        cursor = cnx.cursor()

        sql = "INSERT INTO logrobogqs(Id, Data, nomePDF, LOG, status) VALUES(%s, %s, %s, %s, %s)" 
        valores = (str(uuid.uuid4()), datetime.today(), nome_pdf, values, status)

        cursor.execute(sql, valores)
        cnx.commit()
        print('Salvo com sucesso no banco de dados')

    finally:
        cnx.close()
