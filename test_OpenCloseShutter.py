import os
import pyautogui
import time
import pymsgbox

#iniciando teste
pymsgbox.alert ('O teste será iniciado em 3 segundos...', 'Atenção!', timeout = 3000)

# abrindo aplicacao
os.startfile('E:\\Automação\\API_CheckScanner\\win\\ambienteTeste\\API_AppTest.exe')
time.sleep(1.5)

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

#abre e fecha shutter 'x' vezes
i = '0'
for i in range(10):
    pyautogui.write('8')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.write('9')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')

pyautogui.write('2')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.write('SERV')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('enter')

#finalizando teste
pymsgbox.alert ('O teste será finalizado em 3 segundos...', 'Atenção!', timeout = 3000)

# fechando aplicacao
pyautogui.hotkey('alt', 'f4')
