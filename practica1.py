print("Hola!")
print("¡Bienvenido a Fundamentos de Programación en Python!")
print("ESTO ES EL MODO SANDBOX.")
print(True > False)
print(True < False)
"""pitagoras"""
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
"""Para resolver funcion cuadratica"""
x = float(-1)
y=3*x**3-2*x**2+3*x-1
print("y =", y)
"""para agregar valores"""
algo = input("Dime algo...")
print("Mmm...", algo, "...¿En serio?")
"""Agregar numeros flotante"""
algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)
"""pitagoras ingresando el valor por teclado"""
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)
"""Unir arrays"""
nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")
"""HAcer figuras"""
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
""" convertir un numero a una cadena,"""
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))
"""Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16."""
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
x = min + dura
y = x//60
hora += y
fin = x-(60*y)
r = hora//24
final= hora-(24*r)
print(str(final)+":"+str(fin))
