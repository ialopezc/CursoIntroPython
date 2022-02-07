sum = 1 + 2
print(sum)

print('Hola desde la consola')


sum = 1 + 2  # 3
product = sum * 2
print(product)


# int, plutón era considerado un planeta pero ya es muy pequeño
planetas_en_el_sistema_solar = 8
distancia_a_alfa_centauri = 4.367  # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11"  # string

distancia_a_alfa_centauri = 4.367  # Parece un decimal flotante

type(distancia_a_alfa_centauri)

left_side = 10
right_side = 5
left_side / right_side  # 2

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())


# print("Today's date is: " + date.today())
print("Today's date is: " + str(date.today()))


print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
# print(first_number + second_number)
print(int(first_number) + int(second_number))