# Bootcamp - Dio - BairesDev - Machine Learning Practitioner

## Sistema de Assistência Virtual

### Descrição

Este projeto `assistencia_virtual` é composto por dois scripts principais: `text-to-speech.py` e `speech-to-text.py`. Ambos utilizam bibliotecas de reconhecimento de fala e síntese de voz para interagir com o usuário de maneira eficiente e amigável.

### Funcionalidades

### `text-to-speech.py`

1. **Captura de Texto e Conversão para Áudio**:
   - Captura texto digitado pelo usuário.
   - Converte o texto para áudio em Português do Brasil (`pt-BR`) e Inglês dos Estados Unidos (`en-us`).
   - Usa a biblioteca `pyttsx3` para a conversão de texto em fala.
   - As vozes utilizadas são `Microsoft Daniel` para Português e `Microsoft David` para Inglês.

2. **Interação Contínua com o Usuário**:
   - Permite que o usuário continue gerando novos áudios até que decida sair do sistema digitando a tecla "Q" ou "q".
   - Fornece feedback visual e auditivo das ações realizadas.

3. **Formatação de Texto**:
   - Utiliza a biblioteca `colorama` para formatar o texto exibido no terminal com diferentes cores, destacando mensagens importantes.

### `speech-to-text.py`

1. **Captura de Áudio**:
   - Usa a biblioteca `sounddevice` para capturar áudio do microfone.
   - Converte o áudio capturado para um formato compreensível pelo reconhecedor de fala.

2. **Reconhecimento de Fala**:
   - Utiliza a biblioteca `speech_recognition` para transcrever o áudio capturado para texto.
   - O reconhecimento de fala é configurado para o idioma Português do Brasil (`pt-BR`).

3. **Síntese de Voz**:
   - Usa a biblioteca `pyttsx3` para converter texto em fala.
   - Suporta dois idiomas: Português do Brasil (`pt-BR`) e Inglês dos Estados Unidos (`en-us`).
   - As vozes utilizadas são `Microsoft Daniel` para Português e `Microsoft David` para Inglês.

4. **Interação com o Usuário**:
   - Exibe um menu para o usuário com opções de abrir o Google, Wikipedia, YouTube ou sair do programa.
   - Captura a escolha do usuário e responde adequadamente, abrindo o navegador para a opção escolhida ou finalizando o programa.
   - Utiliza a biblioteca `webbrowser` para abrir links no navegador.

5. **Feedback por Voz**:
   - Fornece feedback auditivo das ações realizadas, falando em Português e Inglês.

6. **Formatação de Texto**:
   - Utiliza a biblioteca `colorama` para formatar o texto exibido no terminal com diferentes cores, destacando mensagens importantes.

### Organização do Código

### `text-to-speech.py`

- **Importações Necessárias**: Importa bibliotecas essenciais como `pyttsx3`, `os`, `googletrans`, `colorama`, `pygame`, `re`, `time` e `sys`.
- **Definições de Funções**:
  - `text_to_speech(text, voice_id, output_file)`: Converte texto em áudio.
  - `speak(text, lang="pt-br")`: Converte texto em fala usando `pyttsx3`.
  - `clear_terminal()`: Limpa o terminal.
  - `get_valid_text()`: Obtém e valida o texto digitado pelo usuário.
  - `main()`: Função principal que gerencia a interação com o usuário e a conversão de texto para áudio.

### `speech-to-text.py`

- **Importações Necessárias**: Importa bibliotecas essenciais como `sounddevice`, `speech_recognition`, `pyttsx3`, `os`, `sys`, `time`, `webbrowser` e `colorama`.
- **Definições de Funções**:
  - `get_audio()`: Captura e transcreve áudio do microfone.
  - `speak(text, lang="pt-br")`: Converte texto em fala usando `pyttsx3`.
  - `clear_terminal()`: Limpa o terminal.
  - `show_menu()`: Exibe o menu de opções para o usuário.
  - `get_user_choice()`: Captura a escolha do usuário.
  - `respond(choice)`: Responde à escolha do usuário com ações apropriadas.

### Exemplo de Uso

### `text-to-speech.py`
Ao executar o script `text-to-speech.py`, o usuário poderá digitar o texto que deseja converter em áudio. O sistema irá gerar e reproduzir os áudios em Português e Inglês e permitirá que o usuário continue gerando novos áudios até decidir sair digitando "Q".

### `speech-to-text.py`
Ao executar o script `speech-to-text.py`, o usuário verá um menu no terminal, onde poderá escolher entre abrir o Google, Wikipedia, YouTube ou sair do sistema. O assistente virtual capturará a escolha, fornecerá feedback por voz e realizará a ação correspondente.

### Considerações Finais

Este projeto visa proporcionar uma experiência de usuário eficiente e amigável, utilizando tecnologias modernas de reconhecimento de fala e síntese de voz.

### Observações

Para que o projeto assistencia_virtual funcione corretamente, é necessário ter o FFmpeg instalado na sua máquina. Caso você não tenha o FFmpeg, siga os passos abaixo:

1. Realize o download do FFmpeg no [site oficial](https://ffmpeg.org/download.html).
2. Extraia o conteúdo do arquivo zip para uma pasta de sua preferência, por exemplo, `C:\FFmpeg`.
3. Adicione o caminho `C:\FFmpeg\bin` (ou o caminho da pasta onde você extraiu o FFmpeg) às Variáveis de Ambiente do Sistema ou do Usuário.
   - No Windows:
     1. Abra o **Painel de Controle** e vá em **Sistema e Segurança** > **Sistema** > **Configurações avançadas do sistema**.
     2. Clique em **Variáveis de Ambiente**.
     3. Em **Variáveis do Sistema**, localize e selecione a variável `Path`, depois clique em **Editar**.
     4. Clique em **Novo** e adicione o caminho `C:\FFmpeg\bin`.
     5. Clique em **OK** em todas as janelas para salvar as alterações.
4. Verifique a instalação abrindo um terminal e digitando `ffmpeg -version` para confirmar se o FFmpeg está corretamente instalado e disponível no `Path`.

Seguindo esses passos, você estará pronto para utilizar o projeto assistencia_virtual no vscode ou outro editor de códigos, sem problemas!