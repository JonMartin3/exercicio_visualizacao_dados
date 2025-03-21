import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())
print(df.info())

# Histograma

plt.figure(figsize=(8,5))
sns.histplot(df["Nota"], bins=10, kde=True)
plt.title("Distribuição das Avaliações dos Produtos")
plt.xlabel("Nota do Produto")
plt.ylabel("Frequência")
plt.show()


# Dispersão - Melhorar

sns.jointplot(y=df["Desconto"], x=df["Qtd_Vendidos_Cod"], kind='scatter')
plt.title("Relação entre Desconto e Quantidade Vendida")
plt.show()


# Calor
df_corr = df[['Qtd_Vendidos_Cod', 'Temporada_Cod', 'Marca_Cod']].corr()

plt.figure(figsize=(10,8))
sns.heatmap(df_corr, fmt=".2f", annot=True)
plt.title("Mapa de Calor das Vendas por Temporada e Marca")
plt.xlabel("Marca")
plt.ylabel("Temporada")
plt.show()


# Barra

plt.figure(figsize=(10,5))
sns.barplot(x=df["Marca"][0:60], y=df["Qtd_Vendidos_Cod"])
plt.xticks(rotation=90)
plt.title("Vendas por Marca")
plt.xlabel("Marca")
plt.ylabel("Quantidade Vendida")
plt.show()


# Pizza
materiais = df["Material"][0:8].value_counts()

plt.figure(figsize=(7,7))
plt.pie(materiais, labels=materiais.index, autopct="%1.1f%%", startangle=90)
plt.title("Distribuição das Vendas por Material")
plt.show()


# Densidade
plt.figure(figsize=(8,5))
sns.kdeplot(df["Nota"], fill=True)
plt.title("Distribuição de Notas dos Produtos")
plt.xlabel("Nota")
plt.ylabel("Densidade")
plt.show()


# Regressão - Melhorar
plt.figure(figsize=(8,5))
sns.regplot(y=df["Nota"], x=df["Qtd_Vendidos_Cod"])
plt.title("Notas dos Produtos x Quantidade Vendida")
plt.ylabel("Nota")
plt.xlabel("Quantidade Vendida")
plt.show()
