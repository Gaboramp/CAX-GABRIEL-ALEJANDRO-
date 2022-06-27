print('Welcome to Miscelanea Gabs')
print('What do you want order?')
numero1=(input('enter your article:'))
numero2=int(input('enter the price:'))
numero3=(input('enter your article:'))
numero4=int(input('enter the price:'))
numero5=(input('enter your article:'))
numero6=int(input('enter the price:'))
numero7=(input('enter your article:'))
numero8=int(input('enter the price:'))
numero9=(input('enter your article:'))
numero10=int(input('enter the price:'))
resultado=numero2+numero4+numero6+numero8+numero10

print('Subtotal:',resultado)
bat=.16
Iva=bat*resultado
print('VAT:',Iva)
total=Iva+resultado
print('Total:',total)
print("Thankyou for buy in Miscelanea Gabs ")