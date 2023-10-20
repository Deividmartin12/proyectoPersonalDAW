import pymysql

def obtener_conexion():
    return pymysql.connect(host='DavidCornejo.mysql.pythonanywhere-services.com',
                                user='DavidCornejo',
                                password='davidmartin12',
                                db='DavidCornejo$discos')