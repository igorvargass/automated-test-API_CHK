import os
import pyautogui
import time
import pymsgbox

# iniciando teste
pymsgbox.alert('O teste será iniciado em 3 segundos...',
               'Atenção!', timeout=3000)

# abrindo aplicacao
os.startfile('E:\\Automação\\API_CheckScanner\\win\\ambienteTeste\\API_AppTest.exe')
time.sleep(1.5)

# abrindo comunicacao
pyautogui.write('17')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.write('1')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.write('SERV')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('enter')
time.sleep(1.5)

# deposito 'x' vezes
num_dep_int = 1
num_dep_text = ''
num_dep = 0
for num_dep in range(10):
    pyautogui.write('10')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.write('15')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.write('14')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.write('12')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(1.5)
    num_dep_text = str(num_dep_int)
    pyautogui.write('deposito ' + num_dep_text)
    num_dep_int += 1
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.write('1')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')

# fechando aplicacao
pyautogui.write('2')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.write('SERV')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('enter')

# finalizando teste
pymsgbox.alert('O teste será finalizado em 3 segundos...',
               'Atenção!', timeout=3000)

# fechando aplicacao
pyautogui.hotkey('alt', 'f4')
