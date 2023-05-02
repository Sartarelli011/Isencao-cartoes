# Isenção de cartões

[![NPM](https://img.shields.io/github/license/Sartarelli011/Isencao-cartoes)](https://github.com/Sartarelli011/Isencao-cartoes/blob/main/LICENSE)

## Sobre o Projeto
O projeto foi criado com o intuito de otimizar uma tarefa que eu tinha em um dos meus últimos empregos.
Essa tarefa era realizar filtros em uma base de dados do Excel para descobrir os clientes que deveriam receber a isenção, tanto por bandeira do cartão quanto por total de gastos mensais. Com Python, consegui automatizar essa tarefa.
O projeto é composto por 3 arquivos:
- Main.py
- functions.py
- Cliente_model.py

### Mais detalhes
#### Main.py
a main é o arquivo principal do nosso programa, ela contém a criação da interface que vai conversar com o usuário.

![main](https://github.com/Sartarelli011/Isencao-cartoes/blob/main/assets/main.png)

#### Cliente_model.py
Aqui está a Classe que instancia o Objeto cliente.
![Class Client](https://github.com/Sartarelli011/Isencao-cartoes/blob/main/assets/Cliente_model.png)


#### functions.py
ela contém as funções que são responsáveis pela nossa lógica do projeto.

![functions](https://github.com/Sartarelli011/Isencao-cartoes/blob/main/assets/functions-all.png)

A função Isencao_cartao é responsavel pela lógica desde filtrar os dados como organizar a planilha excel.
![function isenção](https://github.com/Sartarelli011/Isencao-cartoes/blob/main/assets/functions-isencao.png)
![function isenção continuação](https://github.com/Sartarelli011/Isencao-cartoes/blob/main/assets/functions-final-isencao.png)

A função start que da inicio a lógica, passando o caminho do arquivo e o endereço do arquivo para a função Isencao_cartao
![function start](https://github.com/Sartarelli011/Isencao-cartoes/blob/main/assets/functions-start.png)



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
