import pyautogui
import time
import os

try:
    # Abrir o arquivo PDF com o navegador padrão (Microsoft Edge)
    print("Abrindo o arquivo PDF...")
    os.startfile("C:/Users/IgorMonteiro/Documents/csd.pdf")

    # Esperar o PDF carregar (ajuste conforme necessário)
    print("Aguardando o carregamento do PDF...")
    time.sleep(5)

    # Simular a combinação de teclas "Ctrl + Shift + ."
    print("Simulando a combinação de teclas Ctrl + Shift + .")
    pyautogui.hotkey('ctrl', 'shift', '.')

    # Esperar um pouco para garantir que a combinação de teclas foi processada
    print("Aguardando a execução da combinação de teclas...")
    time.sleep(5)

    # Digitar o comando desejado
    print("Digitando o comando no PDF...")
    pyautogui.write("@this document, list 10 Kyndryl responsibilities, 10 periodicity, and the main takeaways that an IT Auditor must know.")

    # Pressionar Enter
    print("Pressionando Enter...")
    pyautogui.press('enter')

    # Esperar um pouco para o comando ser processado (ajuste conforme necessário)
    print("Aguardando o processamento do comando...")
    time.sleep(5)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    print("Programa em execução. O navegador permanecerá aberto. Pressione Ctrl+C para encerrar o script.")

# Loop infinito para manter o programa ativo
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando o script.")
        break

print("Script finalizado.")
