mercadoriaPreco=float(input('Digite o valor da mercadoria'))
percentualDesconto=float(input('Digite o percentual de desconto. Ex: 2 para 2% 5.5 para 5,5%'))

valorDesconto=mercadoriaPreco*(percentualDesconto/100)
valorFinal=mercadoriaPreco-valorDesconto

print(f'O valor do desconto é R${valorDesconto:5.2f}')
print(f'O valor final é R${valorFinal:5.2f}')