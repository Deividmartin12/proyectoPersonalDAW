class Disco:
    id=0
    codigo=""
    nombre=""
    artista=""
    precio=0.00
    genero=""
    

#constructor
    def __init__(self,p_id,p_codig,p_nombre,p_artista, p_precio,p_genero):
        self.id=p_id
        self.codigo=p_codig
        self.nombre=p_nombre
        self.artista=p_artista
        self.precio=p_precio
        self.genero=p_genero

    def obtener_objeto_serializable(self):
        dict_tem=dict()
        dict_tem["id"]=self.id
        dict_tem["codigo"]=self.codigo
        dict_tem["nombre"]=self.nombre
        dict_tem["artista"]=self.artista
        dict_tem["precio"]=self.precio
        dict_tem["genero"]=self.genero
        return dict_tem