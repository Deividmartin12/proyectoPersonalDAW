from bd import obtener_conexion

def obtener_usuario_por_username(username):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, username, password, token FROM usuarios WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def actualizar_token(username, token):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET token = %s WHERE username = %s",
                       (token, username))
    conexion.commit()
    conexion.close()