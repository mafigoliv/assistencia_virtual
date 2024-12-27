import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import os
import sys
import time
import webbrowser
from colorama import init, Fore

# Inicializa o Colorama
init()

# Definir cores para o texto
class Colors:
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    YELLOW = Fore.YELLOW
    GREEN = Fore.GREEN
    RED = Fore.RED
    BLUE = Fore.BLUE
    END = Fore.RESET

# Caminho onde os arquivos de áudio serão salvos
content_dir = "D:\\Git\\assistencia_virtual\\content"
if not os.path.exists(content_dir):
    os.makedirs(content_dir)

# Função para obter áudio do microfone usando sounddevice
def get_audio():
    samplerate = 44100
    duration = 5  # segundos
    device_id = 6  # ID do dispositivo de entrada (Microfone)
    channels = 1  # Número de canais ajustado para 1
    print(Colors.CYAN + "Listening..." + Colors.END)

    # Captura o áudio usando sounddevice
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=channels, dtype='int16', device=device_id)
    sd.wait()  # Espera até a gravação terminar

    # Converte o áudio capturado para o formato esperado pela biblioteca de reconhecimento
    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(audio.tobytes(), samplerate, channels)
    said = ""
    try:
        said = recognizer.recognize_google(audio_data, language="pt-BR")
        print(Colors.GREEN + said + Colors.END)
    except sr.UnknownValueError:
        print(Colors.RED + "Desculpe, não consegui entender." + Colors.END)
    except sr.RequestError:
        print(Colors.RED + "Desculpe, o serviço não está disponível" + Colors.END)
    return said.lower()

# Função para falar o texto convertido usando pyttsx3
def speak(text, lang="pt-br"):
    engine = pyttsx3.init()
    # Definir a voz com base no idioma
    voices = engine.getProperty('voices')
    if lang == "pt-br":
        for voice in voices:
            if "Daniel" in voice.name:
                engine.setProperty('voice', voice.id)
                break
    elif lang == "en-us":
        for voice in voices:
            if "David" in voice.name:
                engine.setProperty('voice', voice.id)
                break
    engine.setProperty('rate', 180)  # Velocidade da fala ajustada para 180
    engine.say(text)
    engine.runAndWait()

# Função para limpar o terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para mostrar o menu e obter a escolha do usuário
def show_menu():
    menu_text = (
        "\nEscolha uma opção:\n"
        "1. Google\n"
        "2. Wikipedia\n"
        "3. YouTube\n"
    )
    instruction_text = "\nDigite o número da sua escolha ou aperte a tecla 'Q' para sair do sistema: "
    print(Colors.WHITE + menu_text + Colors.END, end='')  
    print(Colors.CYAN + instruction_text + Colors.END, end='')  

def get_user_choice():
    choice = input().strip().lower()
    return choice

# Função para responder aos comandos
def respond(choice):
    if choice == '1':
        print(Colors.GREEN + "Abre Google... Open Google..." + Colors.END)
        speak("Abre Google", lang="pt-br")
        speak("Open Google", lang="en-us")
        webbrowser.open("https://www.google.com")
        show_menu()  
    elif choice == '2':
        print(Colors.GREEN + "Abre Wikipedia... Open Wikipedia..." + Colors.END)
        speak("Abre Wikipedia", lang="pt-br")
        speak("Open Wikipedia", lang="en-us")
        webbrowser.open("https://www.wikipedia.org")
        show_menu()  
    elif choice == '3':
        print(Colors.GREEN + "Abre YouTube... Open YouTube..." + Colors.END)
        speak("Abre YouTube", lang="pt-br")
        speak("Open YouTube", lang="en-us")
        webbrowser.open("https://www.youtube.com")
        show_menu()  
    elif choice == 'q':
        print(Colors.WHITE + "\nFinalizando o programa... Finishing the program..." + Colors.END)
        speak("Finalizando o programa...", lang="pt-br")
        speak("Finishing the program...", lang="en-us")
        print(Colors.WHITE + "\nAté a próxima! Until next time!" + Colors.END)
        speak("Até a próxima!", lang="pt-br")
        speak("Until next time!", lang="en-us")
        time.sleep(1)
        clear_terminal()
        sys.exit()
    else:
        try:
            if choice.strip() == "":
                print(Colors.YELLOW + "Opção inválida! Campo em branco ou nulo. Invalid option! Blank or null field." + Colors.END)
                speak("Opção inválida! Campo em branco ou nulo.", lang="pt-br")
                speak("Invalid option! Blank or null field.", lang="en-us")
                show_menu()  # Mostrar o menu novamente após a resposta
                speak("Digite o número da sua escolha ou aperte a tecla 'Q' para sair do sistema.", lang="pt-br")
                speak("Enter the number of your choice or press the 'Q' key to exit the system.", lang="en-us")           
            else:
                num_choice = int(choice)
                if num_choice < 1 or num_choice > 3:
                    print(Colors.YELLOW + "Opção inválida! Tente novamente. Invalid option! Try again." + Colors.END)
                    speak("Opção inválida! Tente novamente.", lang="pt-br")
                    speak("Invalid option! Try again.", lang="en-us")
                    show_menu()  # Mostrar o menu novamente após a resposta
                    speak("Digite o número da sua escolha ou aperte a tecla 'Q' para sair do sistema.", lang="pt-br")
                    speak("Enter the number of your choice or press the 'Q' key to exit the system.", lang="en-us")
        except ValueError:
            print(Colors.RED + "Entrada inválida! Digite um número inteiro. Invalid entry! Please enter an integer." + Colors.END)
            speak("Entrada inválida! Digite um número inteiro.", lang="pt-br")
            speak("Invalid entry! Please enter an integer.", lang="en-us")
            show_menu()  # Mostrar o menu novamente após a resposta
            speak("Digite o número da sua escolha ou aperte a tecla 'Q' para sair do sistema.", lang="pt-br")
            speak("Enter the number of your choice or press the 'Q' key to exit the system.", lang="en-us")

# Início do programa
print(Colors.WHITE + '''\n------------------------- Bem-vindo ao Sistema de Assistência Virtual. -------------------------\n''' + Colors.END)

# Exibir o menu e as instruções iniciais com os narradores
show_menu()
speak("Bem-vindo ao Sistema de Assistência Virtual. Digite o número da sua escolha ou aperte a tecla 'Q' para sair do sistema.", lang="pt-br")
speak("Welcome to the Virtual Assistance System. Enter the number of your choice or press the 'Q' key to exit the system.", lang="en-us")

# Loop principal para mostrar o menu e responder aos comandos
while True:
    choice = get_user_choice()
    respond(choice)
    if choice == 'q':
        break
