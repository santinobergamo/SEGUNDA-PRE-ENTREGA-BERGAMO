class Cliente():

    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.documento = input("Ingrese su DNI: ")
        self.direccion = input("Ingrese su direccion: ")
        self.mail = self.ingresar_mail()
        self.preferencias = input("Ingrese sus intereses: ")
        self.compra = ""
        self.tienda = input("En que tieda compro? ")

    def ingresar_mail(self):
        while True:
            mail = input("Ingrese su mail: ")
            if "@" in mail:
                return mail
            else:
                print("ERROR!, el mail debe contener '@', intente de nuevo.")
    


    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nDNI: {self.documento}\nEmail: {self.mail}\nDireccion: {self.direccion}\nPreferencias: {self.preferencias}\nCompro en: {self.tienda}\nCompro: {self.compra}"





