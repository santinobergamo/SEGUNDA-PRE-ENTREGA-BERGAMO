from Paquete1.Modulo1 import Cliente

def main():
    
    cliente = Cliente(
        nombre="Santino",
        apellido="Bergamo",
        documento="46579301",
        direccion="av caseros 123",
        mail="santinobergamo@gmail.com",
        preferencias="Tecnologia",
        tienda="Mercado Libre"
    )


    cliente.ingresar_compra("Televisor")

    
    print(cliente)

if __name__ == "__main__":
    main()
