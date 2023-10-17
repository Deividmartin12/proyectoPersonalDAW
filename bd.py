import pymysql

def obtener_conexion():
    return pymysql.connect(host='DavidCornejo.mysql.pythonanywhere-services.com',
                                user='DavidCornejo',
                                password='123456789',
                                db='DavidCornejo$discos')