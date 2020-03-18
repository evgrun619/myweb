import mysql.connector
from mysql.connector import errorcode


def executesql(sql,val):
    try:


        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                  host='127.0.0.1',
                                  database='myweb')
        mycursor = cnx.cursor()
        if not val:
            print(sql)
            print(val)
            mycursor.execute(sql, val)
        else:
            mycursor.execute(sql)
        dataout = mycursor.fetchall()
        cnx.commit()
        mycursor.close()
        cnx.close
        return dataout
    except Exception as e:
        print(e)





