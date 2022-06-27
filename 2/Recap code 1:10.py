#comentarios son lineas que no se ejecutan y son de uso del progamador 

print('hola')
print('hola')
print('hola')
print('hola')
print('hola')
print('hola')
print('hola')

#constantes tiene informacion que no cambia 

pie=3.1416

#variable por la que la informacion que contiene puede cambiar 

fecha=7
fecha=8

#fecha=echa+1

#int o integers enteros

entero=45
  
flotante=456.5

#string o cadenas

ejemplo1="hola"
ejemplo2="nada tomo clase"
ejemplo3="123445 y letras y etc"

#bool o boolean o booleanos   evaluan un falso verdaero

aprobado=True
reprobadotodogrupo=False

#comandos


#print(mensajes):es mandar a la consola informacion del codigo   

#print:para imprimir datos ya guardados en variables/const
print(ejemplo1)
print(aprobado)
print(ejemplo3)
print(fecha)

print(ejemplo1,aprobado,ejemplo3,fecha)

#para imprimir algo directamente

print('hola k hace')
print(3234543)

#print combinado

print('el mensaje enviado fue:',ejemplo1)
print(fecha,"de enero")
print('primer mensaje',ejemplo1,"segundo mensaje",ejemplo2)

#input()permite que el usurario ingrese informacion al codigo,el codigo no avanza hasta que detecte un enter en el teclado 

nombre=input()
print("hola",nombre)

apellido=input('ingrese su apellido')
print("su nombre completo es:",nombre,apellido)

#solo ingresa cadenas(strings)

num=input('ingrese su numero')
print("el numero 10 veces es:",(10*num))

#int()sirve para convertir un string en un int
#float (sirve para convertir un string en un FLOAT)
num=int(input('ingrese numero'))
print('el numero 10 veces es:',(10*num))



#while()es una estructura que permite repetri un codigo practicamente de forma infinita 

#evaluan para falso o verdadero 

while True:
  input()
  print("hola")
#compradores
#==identico
#><mayor o menor
#!=diferente
#= >= o <=mayor o igual  menor o igual



zeta=int(input("numero: "))

while(zeta>=5):
  print('tu numero es mayor o igual que 5')
  

pasw=input("password: ")

while (pasw!='hola'):
  print("volver a intentar")