from Paquete1.Modulo1 import Cliente

def main():
    clientes = []

    while True:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        documento = input("Ingrese su DNI: ")
        direccion = input("Ingrese su direccion: ")
        mail = ingresar_mail()
        preferencias = input("Ingrese sus intereses: ")
        tienda = input("En que tienda compro? ")
        
        cliente = Cliente(nombre, apellido, documento, direccion, mail, preferencias, tienda)

        compra = input("¿Qué llevó? ")
        cliente.ingresar_compra(compra)

        clientes.append(cliente)

        continuar = input("¿Desea ingresar información para otro cliente? (s/n): ")
        if continuar.lower() == 's':
            continue
        else:
            continuar.lower() == 'n'
            break
        
    
    for cliente in clientes:
        print("------------------------------------------------")
        print(cliente)

def ingresar_mail():
    while True:
        mail = input("Ingrese su mail: ")
        if "@" in mail:
            return mail
        else:
            print("ERROR!, el mail debe contener '@', intente de nuevo.")
        


if __name__ == "__main__":
    main()
