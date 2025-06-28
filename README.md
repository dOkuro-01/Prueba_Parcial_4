NOTA: en los ejemplos, las letras con negrita y en rojo significan que son datos
ingresados por teclado.
Haga un programa que permita generar un menú de reservas para la tienda
“Zapatillas Strike”. El menú principal debe permitir mostrar 4 opciones:
TOTEM AUTOATENCIÓN RESERVA STRIKE
1.- Reservar zapatillas
2.- Buscar zapatillas reservadas.
3.- Ver stock de reservas.
4.- Salir.
Todas las opciones del menú deben estar implementadas mediante funciones
separadas del código principal (main).
Al ingresar a la opción 1.- Comprar entrada, se debe permitir ingresar
nombre de comprador y s elección de función por separado. Para que la
compra sea exitosa se debe cumplir lo siguiente:
a) El nombre de comprador no debe estar repetido,
b) Para realizar la reserva el cliente, debe digitar la frase secreta
“EstoyEnListaDeReserva” respetando las mayúsculas y minúsculas.
c) hay un stock máximo de 20 reservas, solo una reserva por comprador.
En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
Al ingresar la opción 2.- Buscar zapatillas reservadas, el menú debe permitir
buscar las reservas mediante el nombre. Si la reserva existe, preguntar si pagar un
adicional por la reserva VIP, el cual permite reservar 2 pares de zapatillas
2
Al ingresar la opción 3.- Ver Stock de reservas, el menú debe permitir observar el
stock de zapatillas ya reservadas y cuantas quedan por reservar.
Al ingresar la opción 4.- Salir, el programa debe terminar mostrando:
Programa terminado...
Si se ingresa una opción distinta (que no sea 1, 2, 3 o 4), debe mostrarse:
Debe ingresar una opción válida!!
