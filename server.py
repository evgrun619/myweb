from flask import Flask, render_template, request,redirect
import mysql.connector
from mysql.connector import errorcode
import sqlmodule



try:
    cnx = mysql.connector.connect(user='evgeny',password='0503727699',
                                  host='127.0.0.1',
                                 database='myweb')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()


app = Flask(__name__)



def allowGet(text):
    try:
        uname = "'" + text['uname'] + "'"
        psw = "'" + text['psw'] + "'"

        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                      host='127.0.0.1',
                                      database='myweb')
        mycursor = cnx.cursor()
        mycursor.execute(f'select login_password from myweb.customer where login_name={uname} and login_password={psw}')
        result = mycursor.fetchall()

        if len(result) == 1:
            return True
        else:
            return False
        mycursor.close()

    except IOError:
        print('error')


def InsertNewOrder(text):
    try:
        ORDERID = request.form.get('forderid')
        CONCRETETYPEID = request.form.get('fsugbeton')
        VOLUME = request.form.get('fvolume')
        MSP_MDGM = request.form.get('fmsp_mdgm')
        MOSAFIM = request.form.get('fmosafim')
        SAPAK = request.form.get('fsapak')
        DARGAT_HASIFA = request.form.get('fdargat_hasifa')
        NIDGAM_FROM = request.form.get('fnidgam_from')
        EFIUN_BETON = request.form.get('fefiun_beton')
        GODEL_GARGIR = request.form.get('fgodel_gargir')
        SHITA_HASHPARA = request.form.get('fshita_hashpara')
        NIDGAM_BCOAH = request.form.get('fnidgam_bcoah')
        SHAA_START = request.form.get('fshaa_start')
        SHAA_END = request.form.get('fshaa_start')




        sql = "INSERT INTO myweb.orders_beton (ORDERID, CONCRETETYPEID, SAPAK , VOLUME, MSP_MDGM ,MOSAFIM, DARGAT_HASIFA," + \
              "NIDGAM_FROM , EFIUN_BETON, GODEL_GARGIR, SHITA_HASHPARA, NIDGAM_BCOAH, " + \
              "SHAA_START, SHAA_END)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        val = (ORDERID, CONCRETETYPEID, SAPAK, VOLUME, MSP_MDGM, MOSAFIM, DARGAT_HASIFA, NIDGAM_FROM, EFIUN_BETON, GODEL_GARGIR, SHITA_HASHPARA, NIDGAM_BCOAH, SHAA_START, SHAA_END)
        #print("sql " + sql)
        #print(val)

        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                      host='127.0.0.1',
                                      database='myweb')
        mycursor = cnx.cursor()
        mycursor.execute(sql, val)
        cnx.commit()
        mycursor.close()
        cnx.close

        #sqlmodule.executesql(sql, val)


    except Exception as e:
        print(e)
        return False

    else:
        return  True

def InsertNewOrderRows(text):
    #print("InsertNewOrderRows")
    try:
        ORDERID = request.form.get('forderid')
        MSPMDGM = request.form.get('fmsp_mdgm')


        sql = "INSERT INTO myweb.orders_beton_detail (ORDERID, MSP_MDGM) VALUES (%s,%s)"

        i = int(MSPMDGM)

        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                      host='127.0.0.1',
                                      database='myweb')
        mycursor = cnx.cursor()

        for x in range(i):
            mspmdg =  ORDERID + '/' + str(x + 1)
            val = (ORDERID, mspmdg)
            mycursor.execute(sql, val)
        cnx.commit()
        mycursor.close()
        cnx.close

    except Exception as e:
        print(e)
        return  False
    else:
        return  True



def InsetNewOrderRowsHozek(text):
    try:
        ORDERID = request.form.get('forderid')
        MSPMDGM = request.form.get('fmsp_mdgm')


        sql = ["INSERT INTO myweb.orders_beton_hozek7 (ORDERID, MSP_MDGM) VALUES (%s,%s)",
               "INSERT INTO myweb.orders_beton_hozek28 (ORDERID, MSP_MDGM) VALUES (%s,%s)",
               "INSERT INTO myweb.orders_beton_hozek_more (ORDERID, MSP_MDGM) VALUES (%s,%s)"]
        i = int(MSPMDGM)

        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                      host='127.0.0.1',
                                      database='myweb')
        mycursor = cnx.cursor()
        for y in sql:
            for x in range(i):
                mspmdg =  ORDERID + '/' + str(x + 1)
                val = (ORDERID, mspmdg)
                mycursor.execute(y, val)

        cnx.commit()
        mycursor.close()
        cnx.close

    except Exception as e:
        print(e)
        return  False
    else:
        return  True






def UpdateRowsNtila(text):
    try:
        rowid = request.form.get('rowid')
        ed_orderid = "'"+ request.form.get('ed_orderid') + "'"
        ed_msp_mdgm = "'"+request.form.get('ed_msp_mdgm') + "'"
        ed_vol_azv = "'"+request.form.get('ed_vol_azv') + "'"
        ed_vol_mtz = "'"+request.form.get('ed_vol_mtz') + "'"
        ed_mixer = "'"+request.form.get('ed_mixer') + "'"
        ed_mishl = "'"+request.form.get('ed_mishl') + "'"
        ed_time_exit = "'"+request.form.get('ed_time_exit') + "'"
        ed_time_ntl = "'" +request.form.get('ed_time_ntl') + "'"
        ed_time_ahana = "'"+ request.form.get('ed_time_ahana') + "'"
        ed_someh = "'" + request.form.get('ed_someh') + "'"


        sql = 'update orders_beton_detail set MSP_MDGM='+ ed_msp_mdgm +','+\
                         ' VOLUME_AZVA='+ ed_vol_azv + ','+\
                         ' VOLUME_MZTB=' + ed_vol_mtz + ','+\
                         ' MIXER='+ ed_mixer + ','+\
                         ' MSP_TEUDA=' + ed_mishl + ','+\
                         ' SHAA_EXIT='+ ed_time_exit + ','+\
                         ' SHAA_NTILA='+ ed_time_ntl +','+\
                         ' SHAA_AHANA='+ ed_time_ahana+ ','+\
                         ' SOMEH='+ ed_someh +\
                         ' where MPP=' + rowid + \
                         ' and ORDERID='+ ed_orderid


        #sqlmodule.executesql(sql, val)
        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                  host='127.0.0.1',
                                  database='myweb')
        mycursor = cnx.cursor()
        mycursor.execute(sql)
        cnx.commit()
        mycursor.close()
        cnx.close



    except Exception as e:
        print(e)

def AllowEditHozek(text):
    try:
        orderid = text['forderid']

        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                      host='127.0.0.1',
                                      database='myweb')
        mycursor = cnx.cursor()
        mycursor.execute(f'select orderid from myweb.orders_beton where orderid={orderid} ')
        result = mycursor.fetchall()
        print("result = mycursor.fetchall() :" + str(result))
        if len(result) == 1:
            return True
        else:
            return False
        mycursor.close()

    except IOError:
        print('error')

def Update7day(text):
    try:
        print("Update7day")
        rowid = request.form.get('rowid')
        ed_orderid = "'"+ request.form.get('ed_orderid') + "'"
        ed_msp_mdgm = "'"+request.form.get('ed_msp_mdgm') + "'"
        ed_date_hozek = "'"+request.form.get('ed_date_hozek') + "'"
        ed_oreh = "'"+request.form.get('ed_oreh') + "'"
        ed_gova = "'"+request.form.get('ed_gova') + "'"
        ed_omes = "'"+request.form.get('ed_omes') + "'"
        ed_hozek = "'"+request.form.get('ed_hozek') + "'"



        sql = 'update orders_beton_hozek7  set MSP_MDGM='+ ed_msp_mdgm +','+\
                         ' DATE_HOZEK='+ ed_date_hozek + ','+\
                         ' OREH=' + ed_oreh + ','+\
                         ' GOVA='+ ed_gova + ','+\
                         ' OMES=' + ed_omes + ','+\
                         ' HOZEK='+ ed_hozek +\
                         ' where MPP=' + rowid + \
                         '  and ORDERID='+ ed_orderid



        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                  host='127.0.0.1',
                                  database='myweb')
        mycursor = cnx.cursor()
        mycursor.execute(sql)
        cnx.commit()
        mycursor.close()
        cnx.close



    except Exception as e:
        print(e)

def Update28day(text):
    try:
        print("Update 28 day")
        rowid = request.form.get('rowid')
        ed_orderid = "'"+ request.form.get('ed_orderid') + "'"
        ed_msp_mdgm = "'"+request.form.get('ed_msp_mdgm') + "'"
        ed_date_hozek = "'"+request.form.get('ed_date_hozek') + "'"
        ed_oreh = "'"+request.form.get('ed_oreh') + "'"
        ed_gova = "'"+request.form.get('ed_gova') + "'"
        ed_omes = "'"+request.form.get('ed_omes') + "'"
        ed_hozek = "'"+request.form.get('ed_hozek') + "'"



        sql = 'update orders_beton_hozek28  set MSP_MDGM='+ ed_msp_mdgm +','+\
                         ' DATE_HOZEK='+ ed_date_hozek + ','+\
                         ' OREH=' + ed_oreh + ','+\
                         ' GOVA='+ ed_gova + ','+\
                         ' OMES=' + ed_omes + ','+\
                         ' HOZEK='+ ed_hozek +\
                         ' where MPP=' + rowid + \
                         '  and ORDERID='+ ed_orderid



        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                  host='127.0.0.1',
                                  database='myweb')
        mycursor = cnx.cursor()
        mycursor.execute(sql)
        cnx.commit()
        mycursor.close()
        cnx.close

    except Exception as e:
        print(e)


def UpdateMoreday(text):
    try:
        print("Update more day")
        rowid = request.form.get('rowid')
        ed_orderid = "'"+ request.form.get('ed_orderid') + "'"
        ed_msp_mdgm = "'"+request.form.get('ed_msp_mdgm') + "'"
        ed_date_hozek = "'"+request.form.get('ed_date_hozek') + "'"
        ed_oreh = "'"+request.form.get('ed_oreh') + "'"
        ed_gova = "'"+request.form.get('ed_gova') + "'"
        ed_omes = "'"+request.form.get('ed_omes') + "'"
        ed_hozek = "'"+request.form.get('ed_hozek') + "'"

        sql = 'update orders_beton_hozek_more  set MSP_MDGM='+ ed_msp_mdgm +','+\
                         ' DATE_HOZEK='+ ed_date_hozek + ','+\
                         ' OREH=' + ed_oreh + ','+\
                         ' GOVA='+ ed_gova + ','+\
                         ' OMES=' + ed_omes + ','+\
                         ' HOZEK='+ ed_hozek +\
                         ' where MPP=' + rowid + \
                         '  and ORDERID='+ ed_orderid



        cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                  host='127.0.0.1',
                                  database='myweb')
        mycursor = cnx.cursor()
        mycursor.execute(sql)
        cnx.commit()
        mycursor.close()
        cnx.close

    except Exception as e:
        print(e)



# -------------------------------- @app.route ------------------------------



@app.route('/')
def login():
    return render_template('login.html')


@app.route('/<string:route_name>')
def route(route_name):
    return render_template(f'{route_name}.html')



@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    error = None
    myMessage = 'Your password or login name is wrong !!!!'
    if request.method == 'POST':
        data = request.form.to_dict()
        if allowGet(data):
            return render_template('/index.html')
        else:
            error = 'Invalid username/password'
            return render_template('/login.html', error=error)


@app.route('/', methods=['POST', 'GET'])
def addOrder():
    print("addOrder(): ")
    if request.method == 'POST':
        data = request.form.to_dict()
        if InsertNewOrder(data):
            InsertNewOrderRows(data)
            InsetNewOrderRowsHozek(data)
            #             0        1      2         3            4             5     6           7          8            9       10
            sql = "SELECT MPP ,ORDERID ,MSP_MDGM ,VOLUME_AZVA ,VOLUME_MZTB ,MIXER,MSP_TEUDA ,SHAA_EXIT ,SHAA_NTILA ,SHAA_AHANA ,SOMEH "+\
                  " FROM myweb.orders_beton_detail WHERE ORDERID="
            ORDERID = data["forderid"]

            #print(sql + ORDERID)


            cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                          host='127.0.0.1',
                                          database='myweb')
            mycursor = cnx.cursor()
            mycursor.execute(sql + ORDERID)
            beton = mycursor.fetchall()
            mycursor.close()
            cnx.close()

            return render_template('concreterows.html', beton=beton)
        else:
            return render_template('thankyou.html')


@app.route('/update', methods=['POST','GET'])
def update():

    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            ORDERID = data["ed_orderid"]

            UpdateRowsNtila(data)

            cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                          host='127.0.0.1',
                                          database='myweb')
            #                         0        1      2         3            4             5     6           7          8            9       10
            sql = "SELECT MPP ,ORDERID ,MSP_MDGM ,VOLUME_AZVA ,VOLUME_MZTB ,MIXER,MSP_TEUDA ,SHAA_EXIT ,SHAA_NTILA ,SHAA_AHANA ,SOMEH " + \
                  " FROM myweb.orders_beton_detail WHERE ORDERID="


            # print(sql + ORDERID)
            mycursor = cnx.cursor()
            mycursor.execute(sql + ORDERID)
            beton = mycursor.fetchall()
            mycursor.close()
            cnx.close()

            return render_template('concreterows.html', beton=beton)
    except Exception as e:
        print(e)

@app.route('/show', methods=['GET', 'POST'])
def show():
    error= None
    sqlpress = ['SELECT * FROM myweb.orders_beton_hozek7 where orderid=',
                'SELECT * FROM myweb.orders_beton_hozek28 where orderid=',
                'SELECT * FROM myweb.orders_beton_hozek_more where orderid=']

    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            if AllowEditHozek(data):
                cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                              host='127.0.0.1',
                                              database='myweb')

                mycursor = cnx.cursor()

                if data['press'] == 'press7':
                    sqlpressout = sqlpress[0] + data['forderid']
                    mycursor.execute(sqlpressout)
                    beton = mycursor.fetchall()
                    mycursor.close()
                    cnx.close()
                    return render_template('concretepress7.html', beton=beton)

                elif data['press'] == 'press28':
                    sqlpressout = sqlpress[1] + data['forderid']
                    mycursor.execute(sqlpressout)
                    beton = mycursor.fetchall()
                    mycursor.close()
                    cnx.close()
                    return render_template('concretepress28.html', beton=beton)

                elif data['press'] == 'pressother':
                    print("pressother")
                    sqlpressout = sqlpress[2] + data['forderid']
                    print(sqlpressout)
                    mycursor.execute(sqlpressout)
                    beton = mycursor.fetchall()
                    mycursor.close()
                    cnx.close()
                    return render_template('concretepressmore.html', beton=beton)

            else:
                error = 'Invalid Orderid'
                return render_template('pressconcrete.html', error=error)

    except Exception as e:
        print(e)



@app.route('/update7' , methods=['GET', 'POST']  )
def update7():
    print("update 7 yiom")
    error = None
    try:

        if request.method == 'POST':
            data = request.form.to_dict()

            Update7day(data)

            ORDERID = data["ed_orderid"]
            mpp = data["rowid"]
            sql = 'SELECT * FROM myweb.orders_beton_hozek7 where orderid='+"'" + ORDERID  +"'"

            cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                          host='127.0.0.1',
                                          database='myweb')

            mycursor = cnx.cursor()
            mycursor.execute(sql)
            beton = mycursor.fetchall()
            mycursor.close()
            cnx.close()
            return render_template('concretepress7.html', beton=beton)

    except Exception as e:
        print(e)

@app.route('/update28' , methods=['GET', 'POST']  )
def update28():
    print("update 28 yiom")
    error = None
    try:

        if request.method == 'POST':
            data = request.form.to_dict()

            Update28day(data)

            ORDERID = data["ed_orderid"]
            mpp = data["rowid"]
            sql = 'SELECT * FROM myweb.orders_beton_hozek28 where orderid='+"'" + ORDERID  +"'"

            cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                          host='127.0.0.1',
                                          database='myweb')

            mycursor = cnx.cursor()
            mycursor.execute(sql)
            beton = mycursor.fetchall()
            mycursor.close()
            cnx.close()
            return render_template('concretepress28.html', beton=beton)

    except Exception as e:
        print(e)

@app.route('/updatemore' , methods=['GET', 'POST']  )
def updateMore():
    print("update more  yiom")
    error = None
    try:

        if request.method == 'POST':
            data = request.form.to_dict()
            UpdateMoreday(data)
            ORDERID = data["ed_orderid"]
            mpp = data["rowid"]
            sql = 'SELECT * FROM myweb.orders_beton_hozek_more where orderid='+"'" + ORDERID  +"'"

            cnx = mysql.connector.connect(user='evgeny', password='0503727699',
                                          host='127.0.0.1',
                                          database='myweb')

            mycursor = cnx.cursor()
            mycursor.execute(sql)
            beton = mycursor.fetchall()
            mycursor.close()
            cnx.close()
            return render_template('concretepressmore.html', beton=beton)

    except Exception as e:
        print(e)
