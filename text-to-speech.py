import pyttsx3
import os
from googletrans import Translator
from colorama import init, Fore
import pygame
import re
import time
import sys

# Inicializa o Colorama
init()

# Definir cores para o texto
class Colors:
    WHITE = Fore.WHITE
    CYAN = Fore.CYAN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    GREEN = Fore.GREEN
    END = Fore.RESET

# Função para converter texto em áudio
def text_to_speech(text, voice_id, output_file):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', 180)  # Velocidade da fala ajustada para 180
    engine.setProperty('volume', 1.0)  # Definir o volume para o máximo
    engine.save_to_file(text, output_file)
    engine.runAndWait()

# Função para falar o texto usando pyttsx3
def speak(text, lang="pt-br"):
    engine = pyttsx3.init()
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
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    # Exibir mensagem de boas-vindas
    print(Colors.WHITE + '''\n------------------------- Bem-vindo ao Sistema de Assistência Virtual. -------------------------\n''' + Colors.END)
    
    # Mensagens dos narradores de boas-vindas
    speak("Bem-vindo ao Sistema de Assistência Virtual.", lang="pt-br")
    speak("Welcome to the Virtual Assistance System.", lang="en-us")
    
    while True:
        # Exibir mensagem para o usuário digitar o texto ou sair do sistema
        print(Colors.CYAN + "\nDigite o texto que deseja converter em áudio ou aperte a tecla 'Q' para sair do sistema: " + Colors.END, end='')
        
        # Falar a mensagem para o usuário digitar o texto ou sair do sistema
        speak("Digite o texto que deseja converter em áudio ou aperte a tecla Q para sair do sistema.", lang="pt-br")
        speak("Enter the text you want to convert to audio or press the Q key to exit the system.", lang="en-us")
        
        # Função para obter e validar texto do usuário
        def get_valid_text():
            while True:
                text = input().strip()  # Manter o input na mesma linha
                if text.upper() == 'Q':  # Verificar se o usuário deseja sair do sistema
                    print(Colors.WHITE + "\nFinalizando o programa... Finishing the program..." + Colors.END)
                    speak("Finalizando o programa...", lang="pt-br")
                    speak("Finishing the program...", lang="en-us")
                    print(Colors.WHITE + "\nAté a próxima! Until next time!" + Colors.END)
                    speak("Até a próxima!", lang="pt-br")
                    speak("Until next time!", lang="en-us")
                    time.sleep(1)
                    clear_terminal()
                    sys.exit()
                # Verificar se o texto contém apenas letras, incluindo acentos, espaços, traços, underlines e pontos, sem caracteres especiais e números
                elif not re.match("^[A-Za-zÀ-ÿ-. _]*$", text):
                    print(Colors.RED + "Entrada inválida! Não é permitido caracteres especiais ou números. Invalid entry! No special characters or numbers are allowed." + Colors.END)
                    speak("Entrada inválida! Não é permitido caracteres especiais ou números.", lang="pt-br")
                    speak("Invalid entry! No special characters or numbers are allowed.", lang="en-us")
                    print(Colors.CYAN + "\nDigite o texto que deseja converter em áudio ou aperte a tecla 'Q' para sair do sistema: " + Colors.END, end='')
                    speak("Digite o texto que deseja converter em áudio ou aperte a tecla Q para sair do sistema.", lang="pt-br")
                    speak("Enter the text you want to convert to audio or press the Q key to exit the system.", lang="en-us")
                elif len(text) == 0:
                    print(Colors.YELLOW + "Opção inválida! Campo em branco ou nulo. Invalid option! Blank or null field." + Colors.END)
                    speak("Opção inválida! Campo em branco ou nulo.", lang="pt-br")
                    speak("Invalid option! Blank or null field.", lang="en-us")
                    print(Colors.CYAN + "\nDigite o texto que deseja converter em áudio ou aperte a tecla 'Q' para sair do sistema: " + Colors.END, end='')
                    speak("Digite o texto que deseja converter em áudio ou aperte a tecla Q para sair do sistema.", lang="pt-br")
                    speak("Enter the text you want to convert to audio or press the Q key to exit the system.", lang="en-us")
                elif len(text) > 50:  # Definindo o limite de 50 caracteres
                    print(Colors.YELLOW + "O texto deve ter no máximo 50 caracteres. Invalid entry! The text should be no longer than 50 characters." + Colors.END)
                    speak("O texto deve ter no máximo 50 caracteres.", lang="pt-br")
                    speak("Invalid entry! The text should be no longer than 50 characters.", lang="en-us")
                    print(Colors.CYAN + "\nDigite o texto que deseja converter em áudio ou aperte a tecla 'Q' para sair do sistema: " + Colors.END, end='')
                    speak("Digite o texto que deseja converter em áudio ou aperte a tecla Q para sair do sistema.", lang="pt-br")
                    speak("Enter the text you want to convert to audio or press the Q key to exit the system.", lang="en-us")
                else:
                    return text
                
        # Solicitar entrada do usuário
        text = get_valid_text()

        # Traduzir o texto para inglês
        translator = Translator()
        translated_text = translator.translate(text, src='pt', dest='en').text
        
        # Caminho onde os arquivos serão salvos
        output_dir = "D:\\Git\\assistencia_virtual\\content"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Gerar áudio em português (usando a voz do Microsoft Daniel)
        portuguese_voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_PT-BR_DANIEL_11.0'
        portuguese_output_file = os.path.join(output_dir, f"{text}.wav")
        text_to_speech(text, portuguese_voice_id, portuguese_output_file)
        print(Colors.GREEN + f"\nÁudio em português gerado com sucesso em: {portuguese_output_file}" + Colors.END)
        speak("Áudio em português gerado com sucesso!", lang="pt-br")
        
        # Gerar áudio em inglês (usando a voz do Microsoft David)
        english_voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
        english_output_file = os.path.join(output_dir, f"{translated_text}.wav")
        text_to_speech(translated_text, english_voice_id, english_output_file)
        print(Colors.GREEN + f"\nÁudio em inglês gerado com sucesso em: {english_output_file}" + Colors.END)
        speak("Áudio em inglês gerado com sucesso!", lang="en-us")
        
        # Reproduzir os áudios
        pygame.mixer.init()
        pygame.mixer.music.load(portuguese_output_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        
        pygame.mixer.music.load(english_output_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

if __name__ == "__main__":
    main()
