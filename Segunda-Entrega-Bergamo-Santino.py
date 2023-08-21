from Pagina_de_compras.Modulo1 import Cliente
from Pagina_de_compras.Modulo2 import Comprar

def main():
    clientes = []

    while True:
        cliente = Cliente()
        cliente.compra = Comprar(input("¿Qué llevó? ")).compra
        clientes.append(cliente)

        if input("¿Desea ingresar información para otro cliente? (s/n): ").lower() != 's':
            break
    
    for cliente in clientes:
        print("------------------------------------------------")
        print(cliente)

if __name__ == "__main__":
    main()









