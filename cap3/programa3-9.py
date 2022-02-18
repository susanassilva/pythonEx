#programa 3-9
dias=int(input('Insira os dias'))
horas=int(input('insira as horas'))
minutos=int(input('insira os minutos'))
segundos=int(input('insira os segundos'))
resultado=(dias*86400)+(horas*3600)+(minutos*60)+segundos

print(resultado, 'segundos')
''' 2a alternativa
resultado2= dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print(resultado2, 'segundos')
'''
