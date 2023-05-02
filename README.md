# Isenção de cartões

[![NPM](https://img.shields.io/github/license/Sartarelli011/Isencao-cartoes)](https://github.com/Sartarelli011/Isencao-cartoes/blob/main/LICENSE)

## Sobre o Projeto
O projeto foi criado com o intuito de otimizar uma tarefa que eu tinha em um dos meus ultimos empregos.
Essa tarefa era, realizar filtros em uma base de dados excel para descobrir os clientes que deveriam receber a isenção, tanto por bandeira do cartão como total de gastos mensais. com python consegui automatizar essa tarefa.
O projeto é composto por 3 arquivos:
- Main.py
- functions.py
- Cliente_model.py



## tecnologias utilizadas
- numpy
- panda
- Tkinter
- pyinstaller



## Instalação
```bash
# clonar repositório
git clone https://github.com/Sartarelli011/Isencao-cartoes.git

#entrar na pasta do projeto
cd Isencao-cartoes

#instalar dependencias
pip install -r requirements.txt

#transformar o arquivo em executavel
pyinstaller --onefie -w /caminho onde se encontra o arquivo/ Main.py
```
depois disso vai ser criado um diretório dist com o executavel dentro.

# autor do projeto
Gabriel Sartarelli Jaccoud
