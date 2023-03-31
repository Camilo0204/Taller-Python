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

"""6) Escriba un programa que lea un número entero del usuario. Entonces
 su programa deberíamostrar un mensaje indicando si el entero es par o impar."""

numero = int(input('Inserte un numero entero:'))

if numero >=1:
   if numero%2 == 0:
    print(numero," es par")
   else:
    print(numero,"es impar")
else:
    print("el valor no es correcto")
"""7) Comúnmente se dice que un año humano equivale a 7 años caninos. Sin embargo, esto
la conversión simple no reconoce que los perros alcanzan la edad adulta en aproximadamente dos
años. Como resultado, algunas personas creen que es mejor contar cada uno de los dos primeros
años humanos como 10.5 años de perro, y luego cuente cada año humano adicional como 4 años de perro
años."""

humano = int(input('Ingrese la edad de un perro en años humanos: '))
	
if humano <= 2:
	edadPerro = humano * 10.5
else:
	edadPerro = 21 + (humano - 2)*4

print('La edad del perro es: ', edadPerro)

if humano <= 0:
	print('la edad debe ser mayor a cero \n')
"""8) En este ejercicio, creará un programa que lea una letra del alfabeto de la
usuario. Si el usuario ingresa a, e, i, o o u entonces su programa debería mostrar un mensaje
indicando que la letra ingresada es una vocal. Si el usuario ingresa y entonces su programa
debería mostrar un mensaje indicando que a veces y es una vocal, y a veces y es
una consonante. De lo contrario, su programa debería mostrar un mensaje que indique que el
letra es una consonante."""        
vocal = ('a', 'e', 'i', 'o', 'u')
consonante = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
while True:
  letra = input("ingrese una letra:\n")
  if letra.lower() == 'y':
    print("Y algunas veces es vocal y otra consonante.\n")
  elif letra in vocal:
    print("%s es una vocal.\n" % (letra.upper()))
  elif letra in consonante:
    print("%s es una consonante.\n" % (letra.upper()))
  else:
    print("el calor ingresado no es valido.\n")
    break
"""9) Un triángulo se puede clasificar en función de la longitud de sus lados como isósceles
equiláteros o escaleno. Los 3 lados de un triángulo equilátero tienen la misma longitud.
Un isósceles el triángulo tiene dos lados que tienen la misma longitud y un tercer lado
que es diferente longitud. Si todos los lados tienen diferentes longitudes, entonces el
triángulo es escaleno. Escriba un programa que lea las longitudes de 3 lados de un
triángulo del usuario. Muestra un mensaje que indica el tipo de triángulo."""

print("ingrese las longitudes de los lados del triangulo ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("el triangulo es Equilatero")
elif x==y or y==z or z==x:
	print("el triangulo es isosceles")
else:
	print("el triangulo es escaleno")
	
"""10) Las personas que aparecen en los billetes en los Estados Unidos se enumeran en la
siguiente Tabla. Escriba un programa que comience leyendo la denominación de un billete
del usuario. Luego, su programa debe mostrar el nombre de la persona que aparece en el
billete de la cantidad ingresada. Se debe mostrar un mensaje de error apropiado si no existe tal nota."""
valor = int(input('Ingrese la denominacion de billete: $'))

nom = ""

if valor == 1:
	nom = 'George Washington'
if valor == 2:
	nom = 'Thomas Jefferson'
if valor == 5:
	nom = 'Abraham Lincoln'
if valor == 10:
	nom = 'Alexander Hamilton'
if valor == 20:
	nom = 'Andrew Jackson'
if valor == 50:
	nom = 'Ulysses S. Grant'
if valor == 100:
	nom = 'Benjamin Franklin'
	
if nom == '':
	print('Cantidad erronea, ingresa nueva cantidad.')
else:
	print('El personaje en la denomicacion es:',(nom))
"""11) Escriba un programa que muestre una tabla de conversión de temperatura para
grados Celsius y grados Fahrenheit. La tabla debe incluir filas para todas las
temperaturas entre 0 y 100 grados centígrados que son múltiplos de 10 grados
centígrados. Incluir apropiado encabezados en sus columnas. La fórmula para
convertir entre grados Celsius y grados Fahrenheit se pueden encontrar en internet."""
print('Celsius', 'Fahrenheit')

for num in range(1, 11):
    celsius = num * 10
    print(celsius, end='      ')
    fahrenheit = 1.8 * celsius + 32
    print(fahrenheit, end=' ')
    print('\n')

"""12) Un minorista en particular tiene un 60 por ciento de descuento en una variedad de
artículos descontinuados.
Al minorista le gustaría ayudar a sus clientes a determinar el precio reducido
de la mercancía al tener una tabla de descuentos impresa en el anaquel que muestra los 
precios originales y los precios después de aplicado el descuento. Escribe un programa que
usa un ciclo para generar esta tabla, mostrando el precio original, el monto del descuento,
y el nuevo precio para compras de $4.95, $9.95, $14.95, $19.95 y $24.95. Asegurar
que los importes de descuento y los nuevos precios se redondean a 2 decimales cuando
se muestran."""

print('Precio   | Descuento | Precio Final')
print('--------------------------------------------')
Original = 4.95
while Original <= 24.95:
    Descuento = Original * 0.60
    PrecioFinal = Original - Descuento
    print(' $%.2f''     |'  %Original, '$%.2f''     |' %Descuento, '$%.2f' %PrecioFinal )
    Original = Original + 5
"""13) En este ejercicio creará un programa que calcula el promedio de una colección de valores
ingresados ​​por el usuario. El usuario ingresará 0 como valor centinela para indicar que no
se proporcionarán más valores. Su programa debe mostrar un apropiado mensaje de error si el
primer valor introducido por el usuario es 0."""
def Promedios():
  my_list = []
  prom  = 0
  count = 0
  Total = 0
  import sys
  print("Dame un Numero.")
  NumberGiven = int(sys.stdin.readline())
  while NumberGiven != 0:
      count +=1
      my_list.append(NumberGiven)
      print ("Dame otro numero:")
      NumberGiven = int(sys.stdin.readline())
      #Cuando termine, los componentes en la lista deben agregarse en un nuevo valor
      Total = sum(my_list)
      prom = (Total/count)
  else:
      print("El promedio de los números ingresados es", prom)
      #NumberGiven = input("Please give me a number")

Promedios()

"""14) Escribe un programa que calcule el perímetro de un polígono. Comience leyendo los
valores x e y para el primer punto en el perímetro del polígono del usuario. Luego,
continúe leyendo pares de valores x e y hasta que el usuario ingrese una línea en
blanco para coordenada x."""
from math import tan, pi

n_sides = int(input("Ingrese el número de lados: "))
s_length = float(input("Introduzca la longitud de un lado: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("El área del polígono es: ",p_area)

"""15) Escriba un programa que implemente el método de Newton para calcular y mostrar el
cuadradoraíz de un número ingresado por el usuario. El algoritmo para el método de Newton
sigue: Leer x del usuario Inicializar adivinar a x / 2 Mientras que adivinar no es lo
suficientemente bueno Actualizar conjetura para que sea el promedio de conjetura y x / conjetura
Cuando se completa este algoritmo, supongo que contiene una aproximación del cuadrado raíz.
La calidad de la aproximación depende de cómo se defina "lo suficientemente bueno".
En la solución del autor, la conjetura se consideraba suficientemente buena cuando el valor
absoluto de la diferencia entre adivinar ∗ adivinar y x fue menor o igual a 10^12."""

from math import sqrt   #Importado la función de raíz cuadrada del módulo de matemáticas
from math import pow    #Importó la función de potencia del módulo matemático.
 
a=int(input("Introduzca la medida de un lado de un triángulo rectángulo:"))    
b=int(input("Introduzca la medida de otro lado de un triángulo rectángulo:"))    
#La función de entrada se utiliza para tomar la entrada del usuario y se almacena como una cadena.
#que luego se convierte en un número entero usando la función int().
c=sqrt(pow(a,2)+pow(b,2)) #Nosotras hemos implementado la fórmula c = √ (a2 + b2)
print(f"La medida de la hipotenusa es: {c} en base a las medidas de los otros dos lados {a} & {b}")   
