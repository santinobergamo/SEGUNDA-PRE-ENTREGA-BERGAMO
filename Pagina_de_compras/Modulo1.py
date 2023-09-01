class Cliente():
    def __init__(self, nombre, apellido, documento, direccion, mail, preferencias, tienda):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.direccion = direccion
        self.mail = mail
        self.preferencias = preferencias
        self.compra = ""
        self.tienda = tienda

    def ingresar_compra(self, compra):
        self.compra = compra

    def __str__(self):
        return f"El cliente {self.nombre} {self.apellido} ha comprado un {self.compra} en la tienda {self.tienda}."
