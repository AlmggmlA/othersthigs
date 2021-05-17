from datetime import date, time,datetime

from bs4 import BeautifulSoup
import requests
import os

dataAtual = date.today().strftime('%d/%m/%y')
horaAtual = datetime.now().strftime('%H:%M:%S')

diretorio = os.path.abspath('magnetLink.txt')
resultadoLista = []


def extrairLink():
    urlInformada = input('Informe a URL:')
    try:
        response = requests.get(urlInformada)
        url = response.text

        usarURL = BeautifulSoup(url, 'html.parser')
        htmlTexto = usarURL.find_all("input", attrs={"type": "button"})

        for itemHTML in htmlTexto:
            resultadoLista.append(itemHTML['value'])
            print('\nLink magnético extraído:\n{}'.format(itemHTML['value']))

    except requests.exceptions.HTTPError as e:
        print('Erro 01',e)
    except requests.exceptions.InvalidSchema as e:
        print('Erro 02',e)
    except requests.exceptions.RequestException as e:
        print('{} é uma URL inválida!'.format(urlInformada))
    except Exception as e:
        print('Erro encontrado:',e)

def gravarArquivo(caminho):
    tamanho = len(resultadoLista)
    for i in range(tamanho):
        dataAtual = date.today().strftime('%d/%m/%y')
        horaAtual = datetime.now().strftime('%H:%M:%S')
        criarArquivo = open(caminho, 'w')
        criarArquivo.write(dataAtual + ' - ' + horaAtual + '\nARQUIVO GRAVADO - Link {}'.format(i+1) + '\n' + resultadoLista[i] + '\n\n')
        criarArquivo.close()
    print(caminho)

def atualizarArquivo(caminho):
    tamanho = len(resultadoLista)
    for i in range(tamanho):
        dataAtual = date.today().strftime('%d/%m/%y')
        horaAtual = datetime.now().strftime('%H:%M:%S')
        criarArquivo = open(caminho, 'a')
        criarArquivo.write(dataAtual + ' - ' + horaAtual + '\nARQUIVO ATUALIZADO - Link {}'.format(i + 1) + '\n' + resultadoLista[i] + '\n\n')
        criarArquivo.close()
    print(caminho)

def sair():
    escolha = input('\nDeseja sair? pressione "1" para SIM ou "2" para NÃO\n')
    if escolha == '2':
        extrairLink()
        atualizarArquivo(diretorio)
        sair()
    elif escolha == '1':
        pass

extrairLink()
gravarArquivo(diretorio)
sair()