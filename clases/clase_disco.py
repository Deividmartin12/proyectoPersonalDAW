class Disco:
    id = 0
    codigo = ""
    nombre = ""
    artista = ""
    precio = 0.0
    genero = ""

    def __init__(self, p_id, p_codigo, p_nombre, p_artista, p_precio, p_genero):
        self.id = p_id
        self.codigo = p_codigo
        self.nombre = p_nombre
        self.artista = p_artista
        self.precio = p_precio
        self.genero = p_genero

    def obtenerObjetoSerializable(self):
        dict_temp = dict()
        dict_temp["id"] = self.id
        dict_temp["codigo"] = self.codigo
        dict_temp["nombre"] = self.nombre
        dict_temp["artista"] = self.artista
        dict_temp["precio"] = self.precio
        dict_temp["genero"] = self.genero
        return dict_temp