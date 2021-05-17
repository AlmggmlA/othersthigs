# IDENTIFICAR SE O NÚMERO É PRIMO OU NÃO NA MATRIZ.

num2 = [1,2,3,4,5,6,7,8,9,10] #lista com valores predeterminados.
print('Escolha um desses valores para saber se é PRIMO ou não: {}'.format(list(num2)))
num1 = int(input('Informe um número: '))

divisao = 0
lista = num1 in num2 #retorna um valor booleano se encontrar ou não o num1 informado dentro da lista num2.

for i in num2: #irá percorrer toda a lista para verificar se o valor num1 é primo ou não.
    if i < len(num2) and num1 in num2: # Checa se o tamanho da lista está sendo respeitado e se num1 está em num2.
        if num1%num2[i-1]==0:
            divisao +=1 # Vai incrementando a variável divisao para saber quantas vezes o valor informado é divisível.
            i+=1
            lista = True
else:
    if lista == True and num1!=1:
        if divisao == 2: # Os primos só são divididos por 1 e por ele mesmo, por esse motivo ele é divisível duas vezes.
            print('{} é Primo!'.format(num1))
        else:
            print('{} não é primo'.format(num1))
    elif num1 == 1:
        print('{} é Primo!'.format(num1))
    else:
        print('{} não está na lista!'.format(num1))