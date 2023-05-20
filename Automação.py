import pyautogui
import time
import pyperclip


# pyautogui.click > clicar com o mouse
# pyautogui.write > escrever um texto
# pyautogui.press > apertar uma tecla
# pyautogui.hotkey > apertar uma combinação de teclas
# pyautogui.position > saber onde o mouse esta

pyautogui.PAUSE = 1

# Passo 1: Acessar o sistema da empresa
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter')

time.sleep(5)

# Passo 2: Fazer login do sistema

pyautogui.click(x=805, y=470)
pyautogui.write('gabrielcordeiro')
pyautogui.click(x=896, y=585)
pyautogui.write('senha123456')
pyautogui.click(x=921, y=658)


time.sleep(5)
# Passo 3: Baixar a base de dados

pyautogui.click(x=381, y=442)
time.sleep(2)
pyautogui.click(x=880, y=261)
pyautogui.click(x=990, y=715)


time.sleep(5)

# Passo 4: Calcular os indicadores
import pandas

#importar a base de dados

tabela = pandas.read_csv(r"C:\Users\gabri\Downloads\Compras.csv", sep =';')
display(tabela)

#calculo dos indicadores

# total gasto 
total_gasto = tabela['ValorFinal'].sum()
# quantidade 
quantidade = tabela['Quantidade'].sum()
# preço medio
preço_medio = total_gasto / quantidade


# Passo 5: Enviar email  para a diretoria

# entrar no meu email

pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pyautogui.press('enter')

time.sleep(5)

# clicar em escrever

pyautogui.click(x=132, y=275)
time.sleep(2)

# preencher o email

pyautogui.write('gabriel.corde@outlook.com.br')
pyautogui.press('tab') # seleciona o email

pyautogui.press('tab') # Passar para o campo de assunto
pyperclip.copy('Relatório de compras')
pyautogui.hotkey("ctrl", "v")

pyautogui.press('tab') # Passar para o corpo de email

texto = f"""
Prezados,

Segue relatório  de compras

Total gasto = R${total_gasto:,.2f}
Quantidade de produtos = {quantidade:,}
Prço Médio = R${preço_medio:,.2f}


Qualquer dúvida, me comunique   

Att,

Gabriel
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar

pyautogui.hotkey('ctrl', 'enter')


# executar no terminal ('pip install pyautogui')
