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
	
