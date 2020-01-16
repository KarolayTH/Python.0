#x=10
#Pedro tiene x años
#print('Pedro tiene', x, 'años')
#print('pedro tiene {} años' .format(x))  
#print(type(x))

#x='karo'
#print(type(x))


#x=10.1
#print(type(x))
#x=10
#print(x)
#x += 5
#print('10 + 5=', x)
#x *= 10
#print(x)
#x /= 2
#print(x)

#x = x**3 #potencia
#y = x
#x = y//15 #cociente
#print(x)
#x = y % 30 #residuo
#print(x)
#x = x**(0.5)
#print(x)

    #name = input('What\'s your name?\n')
    #age = int(input('How old are you \b?\n'))


#if age<0:
    #print('Error! An age can\'t be negative')

#else:
    #print('hi', name, '\b!')
    #print('you are', age,'years old \b!')
    #if age>18:
        #print('you are allowed to enter')
    #else:
        #print('you sall not pass \b!')


print('\t\t\tAREA DE UN CIRCULO')

radio = float(input('¿ \bCuál es el radio \b?\t'))

if radio < 0:
    print('se requiere de un positivo, intente de nuevo')

elif radio==0:
    print('es un punto')
else:
 
     area = (radio**2)*(22/7)
     print('EL ÁREA DE SU CIRCULO ES', area)




