import os
import pyautogui
import time
import pymsgbox
import logging

TESTNAME = '***OpenClose***' #mudar conforme testes
RET = '(-1)'
# configurando log
logging.basicConfig(
    level=logging.DEBUG,
    filename='E:\\Automação\\API_CheckScanner\\win\\ambienteTeste\\log\\log-teste.log',
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%d-%m-%y %H:%M:%S',
    filemode='a'
    )

# iniciando teste
pymsgbox.alert ('O teste será iniciado em 3 segundos...', 'Atenção!', timeout = 3000)
# abrindo aplicação
try:
    os.startfile('E:\\Automação\\API_CheckScanner\\win\\ambienteTeste\\API_AppTest.exe')
    logging.getLogger(os.startfile)
    logging.debug('TestName: ' + TESTNAME)
    logging.debug('msg: Aplicacao aberta!')
    logging.debug('msg: Teste iniciado!')
except:
    logging.error('msg: Erro ao iniciar a aplicacao! ' + RET)
    logging.info('msg: A aplicacao sera fechada no modo forcado!')
    exit()

time.sleep(1.5)
pyautogui.write('17')
time.sleep(1.5)
pyautogui.press('enter')
time.sleep(1.5)

# abre e fecha comunicação 'x' vezes
i = '0'
for i in range(1):
    pyautogui.write('1')
    time.sleep(1.5)
    pyautogui.press('enter')
    logging.debug('msg: Abrindo comunicacao...')
    time.sleep(1.5)
    pyautogui.write('SERV')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.press('enter')
    logging.debug('msg: Comunicacao aberta.')
    pyautogui.write('2')
    time.sleep(1.5)
    pyautogui.press('enter')
    logging.debug('msg: Fechando comunicacao...')
    time.sleep(1.5)
    pyautogui.write('SERV')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    logging.debug('msg: Comunicacao fechada.')

# finalizando teste
pymsgbox.alert('O teste será finalizado em 3 segundos...',
               'Atenção!', timeout=3000)
logging.debug('msg: Finalizando teste')

# fechando aplicacao
try:
    pyautogui.hotkey('alt', 'f4')
    logging.debug('msg: Teste finalizado!')

except:
    logging.error('msg: Erro ao finalizar a aplicacao! ' + RET)
    logging.info('msg: A aplicacao sera fechada no modo forcado!')
    exit()
