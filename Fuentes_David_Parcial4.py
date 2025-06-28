def mostrar_menu():
    print("TOTEM AUTOATENCION RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")

def reservar(reservas, stock):
    print("-- Reservar Zapatillas --")
    nombre = input("Nombre del comprador: ").strip()
    clave = input("Digite la palabra secreta para confirmar la reserva: ").strip()
    
    if clave != "EstoyEnListaDeReserva":
        print("La palabra clave es incorrecta. Reserva no realizada.")
        return reservas, stock

    if nombre in reservas:
        print("Ya Hay una reserva a este nombre.")
        return reservas, stock

    if stock < 1:
        print("Lo siento, no hay stock disponible.")
        return reservas, stock

    reservas[nombre] = {"pares": 1, "tipo": "estandar"}
    stock -= 1
    print(f"Reserva realizada exitosamente para {nombre}.")
    return reservas, stock

def buscar(reservas, stock):
    print("-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador que desea buscar: ").strip()
    
    if nombre not in reservas:
        print("No se encontro ninguna reserva con ese nombre.")
        return reservas, stock

    info = reservas[nombre]
    print(f"Reserva encontrada: {nombre} - {info['pares']} par ({info['tipo']}).")
    
    if info["tipo"] == "estandar":
        respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
        if respuesta == "s":
            if stock >= 1:
                reservas[nombre] = {"pares": 2, "tipo": "VIP"}
                stock -= 1
                print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
            else:
                print("No hay stock suficiente para actualizar a VIP.")
        else:
            print("Manteniendo reserva actual.")
    return reservas, stock

def ver_stock(reservas, stock):
    total_reservados = sum(info["pares"] for info in reservas.values())
    print("-- Ver Stock de Reservas --")
    print(f"Pares reservados: {total_reservados}")
    print(f"Pares disponibles: {stock}")

def main():
    stock = 20
    reservas = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-4): ").strip()

        if opcion == "1":
            reservas, stock = reservar(reservas, stock)
        elif opcion == "2":
            reservas, stock = buscar(reservas, stock)
        elif opcion == "3":
            ver_stock(reservas, stock)
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción valida!!")

main()
