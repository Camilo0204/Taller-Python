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
