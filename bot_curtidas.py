'''Bot de curtidas e comantários no Instagram com PyAutoGui

Criar um bot que define qual pagina quer seguir, verifica se a postagem mais atual ainda não foi curtida pelo bot.
Caso uma nova postagem tenha sido feita, ele deve entrar nessa postagem, curtir e comentar algo nela
 1- Navegar até o site https://www.instagram.com
 2- Mover cursor até campo de entrada de usuário.
 2- Entrar com meu usuário
 2- Mover cursor até campo de entrada de senha.
 3- Entrar com a minha senha
 4- Clicar em "login"
 5- Clicar em "not now"
 6- Fechar janela de "salvar senha"
 7- Pesquisar pela pagina
 8- Entrar na pagina
 9- Clicar na postagem
10- Verificar se já curtiu ou não aquela foto
11-Se já tiver curtido, fazer nada e pausar o bot por 24 horas
12-Se não tiver curtido, curtir a foto
13- Se não tiver comentado, comentar na foto
14-Pausar por 24 horas
15-Após 24 horas fazer tudo de novo.'''

import pyautogui
import webbrowser
import pyperclip
from time import sleep

def digitar_usuario(usuario):
    pyperclip.copy(usuario)
    pyautogui.hotkey('ctrl', 'v')

def digitar_senha(senha):
    pyperclip.copy(senha)
    pyautogui.hotkey('ctrl', 'v')

def pesquisa(pagina):
    pyperclip.copy(pagina)
    pyautogui.hotkey('ctrl', 'v')
   

webbrowser.open_new_tab('https://www.instagram.com') # Open browser
sleep(3)
pyautogui.click(759,369, duration=1) # Move and click
sleep(5)
digitar_usuario('willsantos.edf@gmail.com',) # Type User
sleep(1)
pyautogui.click(759,411, duration=1) # Move and click
sleep(1)
digitar_senha('#Willi@m86')# Type password
sleep(2)
#pyautogui.click(877,506, duration=2)
pyautogui.click(880,467, duration=1) # Push login button
sleep(15)
pyautogui.click(671,545, duration=1) # Save your login info?
sleep(5)
pyautogui.click(561,194, duration=1) # Move and click
sleep(1)
pesquisa('luciele_isis') # Type page
sleep(5)
pyautogui.click(584,268, duration=1) # Move and click
sleep(5) # Time to load

# Scroll page
for i in range(3): 
    pyautogui.scroll(-4)
    sleep(1)

pyautogui.click(378,330, duration=1) # Move and click
sleep(5) # Time to load
coracao = pyautogui.locateCenterOnScreen('coracao.jpg') #Find like icon
sleep(1)
#check if photo was liked: #Willi@m86
if coracao is not None:
    sleep(120)
elif coracao == None:
    pyautogui.click(703,600, duration=1)
    sleep(2)
    pyautogui.click(743,602, duration=1)
    sleep(2)
    pyautogui.moveTo(738,719, duration=1)
    sleep(2)
    pyautogui.typewrite('Gostei dessa foto!')
    sleep(2)
    pyautogui.click(1149,719, duration=1)
    sleep(2)

pyautogui.click(1299,624, duration=1)
sleep(3)

pyautogui.click(1348,46, duration=1)
sleep(3)