import pymysql

def obtener_conexion():
    return pymysql.connect(host='dawgb20232.mysql.pythonanywhere-services.com',
                                user='dawgb20232',
                                password='abcDEF$123',
                                db='dawgb20232$discos')