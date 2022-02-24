cigarrosUsados=int(input('Digite a quantidade de cigarros fumados por dia:'))
anos=int(input('Digite a quantidade de anos que fuma:'))
conversaoDias=anos*365


conversaominutos=(cigarrosUsados*10)*conversaoDias
total=conversaominutos/(24*60)
print(f'O tempo de vida perdido em dias foi de {total:5.2f}')