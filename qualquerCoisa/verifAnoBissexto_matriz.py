# VERIFICAR SE O ANO É BISSEXTO OU NÃO
# Para ser considerado BISSEXTO, o ano tem que ser:
# 1) DIVISÍVEL por 4,
# 2) NÃO PODE ser divisível por 100,
# 3) PODE ser divisível por 400.


print('Do ano 2000 a 2021 quais são bissextos?\n')
listAnoBissexto = []

for i in range(2000,2021):
    if i%4 == 0:
        if i%100 == 0 and i%400 != 0:
            i+=1
        elif i%400 == 0:
            listAnoBissexto.append(i)
            i += 1
        else:
            listAnoBissexto.append(i)
            i += 1
    else:
        i += 1
else:
    print('Os anos BISSEXTOS são: {}'.format(listAnoBissexto))
    print('saiu...')