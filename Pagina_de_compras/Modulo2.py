from Pagina_de_compras.Modulo1 import *
class Comprar():
    def __init__(self,compra):
        self.compra = compra

def main():
    clientes = []
    while True:
        cliente = Cliente()
        compra = input("Que llevo? ")
        compra_cliente = Comprar(compra)
        cliente.compra = compra_cliente.compra
        clientes.append(cliente)

        continuar = input("¿Desea ingresar información para otro cliente? (s/n): ")
        if continuar.lower() != 's':
            break
    
    for cliente in clientes:
        print("------------------------------------------------")
        print(cliente)