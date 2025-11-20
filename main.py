from urllib.parse import quote
import pyautogui as pg
import webbrowser
import openpyxl
from time import sleep

pagina = openpyxl.load_workbook('Planilhas.xlsx')
dados = pagina['Planilha1']

for linha in dados.iter_rows():
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    msg = f'Ola, {nome}, este é um teste de automação feito por Julia R, para saber mais entre em contato ate {vencimento.strftime("%d/%m/%Y")} atraves de https://the-internet.herokuapp.com/'
    try:
        link = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(msg)}'
        webbrowser.open(link)
        sleep(10)
        pg.press('enter')
        sleep(1)
        pg.hotkey('ctrl', 'w')
    except Exception:
        print('Ocorreu algum erro.')
        with open('Erros.txt', 'a', encoding='utf-8') as a:
            a.write(f'{nome} - {telefone}\n')
