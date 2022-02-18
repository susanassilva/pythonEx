#questao 3.6

materia1=int(input('Insira a nota da matéria 1: '))
materia2=int(input('Insira a nota da matéria 2: '))
materia3=int(input('Insira a nota da matéria 3: '))

media=(materia1+materia2+materia3)/3
if media >7:
    print("Aprovado, sua média foi: %0.2f" %media)
else:
    print("Reprovado, sua média foi: %0.2f" %media )
