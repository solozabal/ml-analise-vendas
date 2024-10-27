import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Parte 1: Criar e popular o banco de dados
print("Parte 1: Criar e popular o banco de dados")
conexao = sqlite3.connect('dados_vendas.db')
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')
conexao.commit()
conexao.close()
print("Parte 1 concluída")

# Parte 2: Carregar dados no Pandas
print("Parte 2: Carregar dados no Pandas")
conexao = sqlite3.connect('dados_vendas.db')
df_vendas = pd.read_sql_query('SELECT * FROM vendas1', conexao)
conexao.close()
print("Primeiras linhas do DataFrame:")
print(df_vendas.head())
print("\nInformações do DataFrame:")
print(df_vendas.info())
print("\nDescrição estatística:")
print(df_vendas.describe())
print("\nValores ausentes por coluna:")
print(df_vendas.isnull().sum())
print("Parte 2 concluída")

# Parte 3: Análises com Pandas
print("Parte 3: Análises com Pandas")
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
df_vendas['mes'] = df_vendas['data_venda'].dt.month
df_vendas['ano'] = df_vendas['data_venda'].dt.year
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()
print("\nTotal de vendas por categoria:")
print(vendas_por_categoria)
quantidade_vendas_categoria = df_vendas['categoria'].value_counts().reset_index()
quantidade_vendas_categoria.columns = ['categoria', 'quantidade_vendas']
print("\nQuantidade de vendas por categoria:")
print(quantidade_vendas_categoria)
vendas_por_produto = df_vendas.groupby('produto')['valor_venda'].sum().reset_index()
vendas_por_produto = vendas_por_produto.sort_values(by='valor_venda', ascending=False)
print("\nVendas por produto (ordenado por valor):")
print(vendas_por_produto)
vendas_por_mes = df_vendas.groupby('mes')['valor_venda'].sum().reset_index()
print("\nVendas por mês:")
print(vendas_por_mes)
print("Parte 3 concluída")

# Parte 4: Visualizações com Matplotlib e Seaborn
print("Parte 4: Visualizações com Matplotlib e Seaborn")
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

print("Criando gráfico de barras - Total de Vendas por Categoria")
plt.figure(figsize=(8,6))
sns.barplot(x='categoria', y='valor_venda', data=vendas_por_categoria, palette='viridis', hue='categoria', legend=False)
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor de Vendas (R$)')
plt.show()

print("Criando gráfico de pizza - Proporção de Vendas por Categoria")
plt.figure(figsize=(8,8))
plt.pie(vendas_por_categoria['valor_venda'], labels=vendas_por_categoria['categoria'], autopct='%1.1f%%', colors=sns.color_palette('viridis'))
plt.title('Proporção de Vendas por Categoria')
plt.show()

print("Criando gráfico de barras - Quantidade de Vendas por Categoria")
plt.figure(figsize=(8,6))
sns.barplot(x='categoria', y='quantidade_vendas', data=quantidade_vendas_categoria, palette='magma', hue='categoria', legend=False)
plt.title('Quantidade de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Quantidade de Vendas')
plt.show()

print("Criando gráfico de barras - Top 5 Produtos mais Vendidos em Valor")
top5_produtos = vendas_por_produto.head(5)
plt.figure(figsize=(10,6))
sns.barplot(x='valor_venda', y='produto', data=top5_produtos, palette='coolwarm', hue='produto', legend=False)
plt.title('Top 5 Produtos mais Vendidos em Valor')
plt.xlabel('Valor de Vendas (R$)')
plt.ylabel('Produto')
plt.show()

print("Criando gráfico de linha - Vendas ao Longo dos Meses")
plt.figure(figsize=(10,6))
sns.lineplot(x='mes', y='valor_venda', data=vendas_por_mes, marker='o')
plt.title('Vendas ao Longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Valor de Vendas (R$)')
plt.xticks(range(1,13))
plt.show()

print("Criando heatmap - Correlação entre as Variáveis Numéricas")
plt.figure(figsize=(8,6))
sns.heatmap(df_vendas[['valor_venda', 'mes', 'ano']].corr(), annot=True, cmap='Blues')
plt.title('Correlação entre Variáveis Numéricas')
plt.show()

print("Parte 4 concluída")