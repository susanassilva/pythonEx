kmRodados=float(input('Digite a quantidade de km percorridos:'))
dias=int(input('Digite a quantidade de dias alugados:'))

total=(kmRodados*0.15)+(dias*60)
print(f'O valor final do aluguel é de R$ {total:5.2f}')