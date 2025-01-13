# Desafio de Onboarding de Clientes

Este projeto é uma automação para resolver o desafio de onboarding de clientes disponível no site [Automation Anywhere Pathfinder](https://pathfinder.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html). Utilizando a biblioteca Clicknium, o script automatiza o preenchimento de um formulário com dados de clientes fornecidos em um arquivo CSV.

## Funcionalidades

- Abre automaticamente o site do desafio.
- Lê os dados de um arquivo CSV.
- Preenche os campos do formulário com os dados dos clientes.
- Simula cliques e interações para submissão do formulário.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no projeto.
- **Clicknium**: Biblioteca usada para automação de navegadores e interações com a interface gráfica.
- **CSV**: Formato de arquivo para entrada de dados.

## Como Usar

### Pré-requisitos

1. Instale o Python (versão 3.7 ou superior).
2. Instale a biblioteca Clicknium:
   ```bash
   pip install clicknium
   ```
3. Certifique-se de que o arquivo customer-onboarding-challenge.csv está na mesma pasta que o script.
4. Certifique-se de estar logado no site da Automation Anywhere

## Execução 

1. Clone este repositório:
   ```bash
   git clone git@github.com:jonatasdamata/challenge_customer_onboarding.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd challenge_customer_onboarding
   ```
3. Exeute o script 
   ```bash
   python customer_onboarding.py
   ```

## Funcionamento do Script

1. O site do desafio é aberto automaticamente. 
2. O arquivo CSV é lido, linha por linha, para capturar os dados dos clientes. 
3. Cada campo do formulário é preenchido com os valores correspondentes: <br/>
Nome da Empresa <br/>
ID da Empresa <br/>
Contato Principal <br/>
Endereço <br/>
Cidade <br/>
Estado <br/>
CEP <br/>
Email <br/>
Desconto Ativo (Sim ou Não) <br/>
Arquivo do Cliente em Registro (Sim ou Não) <br/>
O formulário é enviado para cada cliente. <br/>
