# VERIFICAR SE O ANO É BISSEXTO OU NÃO
# Para ser considerado BISSEXTO, o ano tem que ser:
# 1) DIVISÍVEL por 4,
# 2) NÃO PODE ser divisível por 100,
# 3) PODE ser divisível por 400.

numero = int(input('Informe o ANO que deseja verificar se é BISSEXTO ou não: '))

if numero%4 == 0:
    if numero%100 == 0 and numero%400 != 0:
        print('{} Não é BISSEXTO!'.format(numero))
    elif numero%400 == 0:
        print('{} é BISSEXTO!'.format(numero))
    else:
        print('{} é BISSEXTO!'.format(numero))
else:
    print('{} Não é BISSEXTO!'.format(numero))
