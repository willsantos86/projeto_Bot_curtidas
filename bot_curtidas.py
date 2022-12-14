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
   




webbrowser.open_new('https://www.instagram.com') # Open browser
pyautogui.click(759,369, duration=5) # Move and click
digitar_usuario('willsantos.edf@gmail.com',) # Type User
pyautogui.click(759,411, duration=2) # Move and click
digitar_senha('#Willi@m86')# Type password
#pyautogui.click(877,506, duration=2)
pyautogui.click(880,467, duration=2) # Push login button
pyautogui.click(671,545, duration=5) # Save your login info?
pyautogui.click(561,194, duration=5) # Move and click
pesquisa('luciele_isis') # Type page
pyautogui.click(584,268, duration=5) # Move and click
sleep(5) # Time to load

# Scroll page
for i in range(3): 
    pyautogui.scroll(-4)
    sleep(1)

pyautogui.click(378,330, duration=5) # Move and click
sleep(2) # Time to load

curtir = pyautogui.locateCenterOnScreen('Nao_curtir.png') #Find like icon

#check if photo was liked: 
if curtir:
    pyautogui.click(curtir[0],curtir[1], duration=3)
else:
    print(f'Foto já foi curtida')

