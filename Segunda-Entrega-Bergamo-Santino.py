<<<<<<< HEAD
from Paquete1.Modulo1 import Cliente
=======
from Pagina_de_compras.Modulo1 import Cliente
from Pagina_de_compras.Modulo2 import Comprar
>>>>>>> d4ecf09c4e637267345e1c238d93a6cbdbde3ff0

def main():
    clientes = []

    while True:
<<<<<<< HEAD
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

=======
        cliente = Cliente()
        
        cliente.compra = Comprar(input("¿Qué llevó? ")).compra
>>>>>>> d4ecf09c4e637267345e1c238d93a6cbdbde3ff0
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
