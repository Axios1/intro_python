#Imprimir en la consola
print("Hola Mundo")

#Declaracion de variables
#El tipo de dato es inferido (determinado a traves del valor)
miNumero = "Cinco"
#El tipo de dato puede cambiar.
miNumero = 5
print("El valor de miNumero es: " + str(miNumero))

#Castings mas comunes
x = str(3)
y = int(3)
z = float(3)

print("El tipo de dato de x es: " + str(type(x)))
print("El tipo de dato de y es: " + str(type(y)))
print("El tipo de dato de z es: " + str(type(z)))

edad = 15

#Condicion
if edad >= 18: 
    print("Eres mayor de edad")
    print("Porque tienes 18 o mas")
else:
    print("No eres mayor de edad")
    print("Porque tienes menos de 18")

#Listas
frutas = ["Manzana", "Fresa", "Mango", "Papoi", "mango"]

print(frutas[0])

#Ciclo for
#Solo recorre arreglos

print("Ciclo for")
indice = 0
for fruta in frutas:
    print("indice: " + str(indice))
    print(fruta)
    indice = indice + 1 

for i in range(7):
    print("Numero: " + str(i))

#len obtiene el numero de elementos de una lista
for i in range(len(frutas)):
    print("Fruta #" + str(i) + " :" + frutas [i])


#FUNCIONES
def mi_funcion():
    print("Estamos dentro de una funcion")

mi_funcion()

#Funcion con parametros
# -Parametros con valor predeterminado
# (Solo se usan si no les mandas valor)
def mi_funcion_con_parametros(palabra_uno = "Palabra uno", palabra_dos = "Palabra dos"):
    print(palabra_uno + " " + palabra_dos)

mi_funcion_con_parametros("Juan", "Pereaz")
mi_funcion_con_parametros("Ana", "garcia")
mi_funcion_con_parametros()