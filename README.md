# 📊 Análise de Vendas com Python 

Este projeto realiza uma análise de vendas utilizando **Python**, **SQLite**, **Pandas**, **Matplotlib** e **Seaborn**. O objetivo é criar um banco de dados de vendas, carregar os dados em um DataFrame do Pandas, realizar análises e gerar visualizações gráficas.

---

## 📁 Estrutura do Projeto

```plaintext
ml-analise-vendas
│
├── venv/               # Ambiente virtual
├── .gitignore
├── LICENSE
├── requirements.txt    # Dependências do projeto
└── main.py             # Script principal

⚙️ Requisitos

Python 3.x
Pandas
Matplotlib
Seaborn
SQLite3

🚀 Instalação

1. Clone o repositório:

git clone https://github.com/solozabal/ml-analise-vendas.git
cd ml-analise-vendas

2. Crie e ative um ambiente virtual:

python -m venv venv
# No Windows
.\venv\Scripts\activate
# No Linux/macOS
source venv/bin/activate

3. Instale as dependências:

pip install -r requirements.txt

▶️ Execução
Para executar o script, certifique-se de que o ambiente virtual está ativado e execute o comando:

python main.py

📝 Descrição do Script
O script main.py realiza as seguintes etapas:

1. Criar e Popular o Banco de Dados
Cria um banco de dados SQLite chamado dados_vendas.db.
Cria a tabela vendas1 e insere dados de vendas.

2. Carregar Dados no Pandas
Carrega os dados da tabela vendas1 em um DataFrame do Pandas.
Exibe as primeiras linhas, informações gerais, descrição estatística e valores ausentes do DataFrame.

3. Análises com Pandas
Converte a coluna data_venda para o tipo datetime.
Extrai o mês e o ano da data da venda.
Analisa o total de vendas e a quantidade de vendas por categoria, produto e mês.

4. Visualizações com Matplotlib e Seaborn
Gera gráficos de barras, gráficos de pizza, gráficos de linha e um heatmap para visualizar os dados.

📊 Visualizações
Total de Vendas por Categoria
Proporção de Vendas por Categoria
Quantidade de Vendas por Categoria
Top 5 Produtos mais Vendidos em Valor
Vendas ao Longo dos Meses
Correlação entre Variáveis Numéricas

📜 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

📬 Contato
Pedro Solozabal
✉️ contato@solozabal.com.br
🔗 Projeto no GitHub