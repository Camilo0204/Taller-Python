"""1)Escriba un programa que le pida al usuario que ingrese su nombre.
El programa debe responder con un mensaje de saludo al usuario, 
utilizando su nombre."""

nombre =str (input("Escriba su Nombre :"))
print("Hola",nombre,"Bienvenido ...") 

"""2)Escriba un programa que le pida al usuario que ingrese el ancho y 
la longitud de una habitación. Una vez los valores han sido leídos, 
su programa debe calcular y mostrar el área de habitación. La longitud
y el ancho se ingresarán como números de coma flotante. Incluir unidades
en su mensaje de solicitud y salida; ya sea pies o metros, dependiendo
de qué unidad con la que se siente más cómodo trabajando. """

largo= float(input('inserte largo de la habitacion :'))
ancho= float(input('inserte ancho de la habitacion :'))
area= print("Area de Habitacion es :",largo*ancho," metros")

"""3) Cree un programa que lea la longitud y el ancho del campo
 de un agricultor del usuario en pies Muestra el área del campo en acres"""
 
largo= float(input('inserte el largo del campo :'))
ancho= float(input('inserte el ancho del campo :'))
area= print("El area del campo en ACRES ES:",largo*ancho/4046.856)

"""4) Escriba un programa que lea un entero positivo, n, del usuario y 
luego muestre la suma de todos los enteros de 1 a n. La suma de los 
primeros n enteros positivos puede ser calculado usando la fórmula: 
sum=(n)(n+1)/2."""
n= int(input('Introduce un número entero:'))
suma=int((n)*(n+1)/(2))
print('La suma de los números anteriores de tipo entero a su número es:',suma)

"""5) Un minorista en línea vende dos productos: widgets y artilugios.
Cada widget pesa 75 gramos Cada artilugio pesa 112 gramos.
Escribe un programa que lea el número de widgets y la cantidad de
artilugios en un pedido del usuario. Entonces tu programa debe calcular
y mostrar el peso total de la orden"""
caja1=0.075
caja2=0.112
widgets=int(input('Ingrese la cantidad de Widgets:'))
artilujio=int(input('Ingrese la cantidad de Artilujio:'))
P1=widgets*caja1
P2=artilujio*caja2
total=P1+P2
print('El peso total a enviar es:',total,'kg')

