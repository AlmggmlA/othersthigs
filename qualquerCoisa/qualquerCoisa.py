

cedula = int(input('Nota:'))   #int(input('Digite a nota: '))
notas = [1,2,5,20,50,100,200]

contador1 = 0
contador2 = 0
contador5 = 0

soma1 = 0
soma2 = 0
soma5 = 0

while cedula in notas:

    if cedula == 1:
        print('A nota escolhida foi: {}'.format(cedula))
        contador1 += 1
        soma1 = cedula * contador1
        cedula = int(input('Nota:'))

    if cedula == 2:
        print('A nota escolhida foi: {}'.format(cedula))
        contador2 += 1
        soma2 = cedula * contador2
        cedula = int(input('Nota:'))
    if cedula == 5:
        print('A nota escolhida foi: {}'.format(cedula))
        contador5 += 1
        soma5 = cedula * contador5
        cedula = int(input('Nota:'))

else:
    somaTotal = soma1+soma2+soma5
    print('\nTOTAL.: {}'.format(somaTotal))
    print('sem mais notas.')
    print('Qtd R$1: {}'.format(contador1) + " Subtotal: {}".format(soma1))
    print('Qtd R$2: {}'.format(contador2) + " Subtotal: {}".format(soma2))
    print('Qtd R$5: {}'.format(contador5) + " Subtotal: {}".format(soma5))