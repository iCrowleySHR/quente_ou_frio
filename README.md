# 🎮 Jogo do Quente ou Frio – Fase 2 (Interface Gráfica em Python)

Versão aprimorada do clássico **“Quente ou Frio”**, agora com **interface gráfica (Tkinter)** e **gráfico de desempenho (Matplotlib)**.  
O jogador tenta adivinhar um número misterioso, recebendo dicas e visualizando suas jogadas ao final.

## 🚀 Funcionalidades
1. **🖥️ Tela Inicial**
   - Exibe o nome do jogo e uma mensagem de boas-vindas.
   - Campo para inserir o **nome do jogador**.
   - Botão **“Iniciar”** para começar.
2. **🎚️ Escolha da Dificuldade**
   - Jogador seleciona a quantidade de **dígitos do número misterioso**.
   - O número é gerado automaticamente dentro do intervalo correspondente:
     - 1 dígito → 0 a 9
     - 2 dígitos → 10 a 99
     - 3 dígitos → 100 a 999
     - 4 dígitos → 1000 a 9999
3. **🎯 Tela de Jogo**
   - Campo para o jogador digitar seu palpite.
   - Mensagens automáticas informam se o número é **maior** ou **menor** que o palpite.
   - Cada tentativa é registrada.
4. **🧾 Registro de Jogadas**
   - Lista que armazena as tentativas no formato: [número_da_tentativa, valor_chutado].
5. **🏆 Tela de Resultado**
   - Exibe o número correto, o total de tentativas e uma mensagem de parabéns personalizada.
6. **📈 Gráfico de Desempenho**
   - Mostra o histórico das jogadas:
     - Eixo X: número da tentativa
     - Eixo Y: valor chutado
   - Gerado com **Matplotlib**, integrado ao **Tkinter**.
7. **🔁 Tela Final – Jogar Novamente**
   - Após o gráfico, o jogador escolhe entre **jogar novamente** ou **sair**.

## ⚙️ Requisitos Técnicos
- Python 3.8+
- Bibliotecas utilizadas:
  - tkinter (nativo do Python)
  - matplotlib

## 🧩 Estrutura do Projeto
📁 quente_ou_frio/
├── app/ 
├── main.py              # Código principal do jogo
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo

## 🧰 Instalação
1. Clone o repositório:
   git clone https://github.com/seuusuario/quente_ou_frio.git
   cd quente_ou_frio
2. Instale as dependências:
   pip install -r requirements.txt
3. Execute o jogo:
   python main.py

## 🧠 Conceitos Envolvidos
- Programação orientada a eventos com Tkinter
- Manipulação de widgets (Labels, Buttons, Entry)
- Uso de variáveis globais para controle do fluxo
- Geração e exibição de gráficos com Matplotlib
- Integração entre interface e visualização de dados

## 💡 Exemplo de Execução
1. Jogador escolhe 3 dígitos  
2. Palpites: 500, 700, 650, 632  
3. Ao acertar, o programa exibe:
   - “Parabéns, [nome]! O número era 632.”
   - Total de tentativas: 4
   - Gráfico de desempenho das jogadas

## 🧾 Licença
Projeto livre para uso educacional e não comercial.  
Créditos: Desenvolvido como exercício de Python + Tkinter + Matplotlib.
