import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados das bases
df_soja_1 = pd.read_csv('soja-valor-da-produo-2023 (1).csv')  # Exemplo de caminho para a Base 1 de Soja
df_soja_2 = pd.read_csv('soja-valor-da-produo-mil-reais.csv')  # Exemplo de caminho para a Base 2 de Soja
df_cama_1 = pd.read_csv('canadeacar-valor-da-produo-2023.csv')  # Exemplo de caminho para a Base 1 de Cama de Açúcar
df_cama_2 = pd.read_csv('canadeacar-valor-da-produo-mil-reais.csv')  # Exemplo de caminho para a Base 2 de Cama de Açúcar

# Garantir que a coluna 'valor' seja numérica para todas as bases
df_soja_1['valor'] = pd.to_numeric(df_soja_1['valor'], errors='coerce')
df_cama_1['valor'] = pd.to_numeric(df_cama_1['valor'], errors='coerce')

# Remover pontos dos valores nas bases de Cama de Açúcar e Soja e converter para numérico
df_soja_2['valor'] = df_soja_2['valor'].str.replace('.', '', regex=False).astype(float)
df_cama_2['valor'] = df_cama_2['valor'].str.replace('.', '', regex=False).astype(float)

# Exibir título geral
st.title("Análise de Produção - Soja e Cama de Açúcar")

# Exibir a Base 1 de Soja - Mapa
st.subheader("Mapa - Valor da Produção de Soja")
st.write("Análise do valor total da produção de soja no estado de Rondônia.")
st.write(df_soja_1)

# Exibir o valor total da produção de soja na Base 1
st.write(f"Valor Total da Produção de Soja em Rondônia: R$ {df_soja_1['valor'].sum():,.2f} ({df_soja_1['unidade'][0]})")

# Gráfico de barras - Base 1 de Soja (Mapa) com Plotly
st.subheader("Gráfico de Barras - Valor da Produção de Soja por Localidade")
fig_bar_soja = px.bar(df_soja_1, x='localidade', y='valor', title="Valor da Produção de Soja por Localidade - Mapa", labels={'valor': 'Valor da Produção (Mil Reais)', 'localidade': 'Localidade'})
st.plotly_chart(fig_bar_soja)

# Exibir a Base 2 de Soja - Série Histórica
st.subheader("Série Histórica - Valor da Produção de Soja")
st.write("Análise do valor total da produção de soja no ano de 2019.")
st.write(df_soja_2)

# Exibir o valor total da produção de soja na Base 2
st.write(f"Valor Total da Produção de Soja em {df_soja_2['periodos'][0]}: R$ {df_soja_2['valor'][0]:,.2f}")

# Gráfico de linha - Base 2 de Soja (Série Histórica) com Plotly
st.subheader("Gráfico de Linha - Evolução do Valor da Produção de Soja (Série Histórica)")
fig_line_soja = px.line(df_soja_2, x='periodos', y='valor', title="Valor da Produção de Soja - Série Histórica", labels={'valor': 'Valor da Produção (Mil Reais)', 'periodos': 'Períodos'})
st.plotly_chart(fig_line_soja)

# Exibir a Base 1 de Cama de Açúcar - Mapa
st.subheader("Mapa - Valor da Produção de Cama de Açúcar")
st.write("Análise do valor total da produção de cama de açúcar no estado de Rondônia.")
st.write(df_cama_1)

# Exibir o valor total da produção de cama de açúcar na Base 1
st.write(f"Valor Total da Produção de Cama de Açúcar em Rondônia: R$ {df_cama_1['valor'].sum():,.2f} ({df_cama_1['unidade'][0]})")

# Gráfico de barras - Base 1 de Cama de Açúcar (Mapa) com Plotly
st.subheader("Gráfico de Barras - Valor da Produção de Cama de Açúcar por Localidade")
fig_bar_cama = px.bar(df_cama_1, x='localidade', y='valor', title="Valor da Produção de Cama de Açúcar por Localidade - Mapa", labels={'valor': 'Valor da Produção (Mil Reais)', 'localidade': 'Localidade'})
st.plotly_chart(fig_bar_cama)

# Exibir a Base 2 de Cama de Açúcar - Série Histórica
st.subheader("Série Histórica - Valor da Produção de Cama de Açúcar")
st.write("Análise do valor total da produção de cama de açúcar no ano de 2019.")
st.write(df_cama_2)

# Exibir o valor total da produção de cama de açúcar na Base 2
st.write(f"Valor Total da Produção de Cama de Açúcar em {df_cama_2['periodos'][0]}: R$ {df_cama_2['valor'][0]:,.2f}")

# Gráfico de linha - Base 2 de Cama de Açúcar (Série Histórica) com Plotly
st.subheader("Gráfico de Linha - Evolução do Valor da Produção de Cama de Açúcar (Série Histórica)")
fig_line_cama = px.line(df_cama_2, x='periodos', y='valor', title="Valor da Produção de Cama de Açúcar - Série Histórica", labels={'valor': 'Valor da Produção (Mil Reais)', 'periodos': 'Períodos'})
st.plotly_chart(fig_line_cama)

# Correlation Analysis
# Supondo que você quer analisar a correlação entre os valores de produção de soja e cama de açúcar em cada período ou localidade

# Merge dos dados de soja e cama de açúcar com base nos períodos ou localidades
merged_data = pd.merge(df_soja_2[['periodos', 'valor']], df_cama_2[['periodos', 'valor']], on='periodos', suffixes=('_soja', '_cama'))

# Calcular a correlação entre os valores de soja e cama de açúcar
correlation = merged_data['valor_soja'].corr(merged_data['valor_cama'])

# Exibir a correlação
st.subheader("Correlação entre Soja e Cama de Açúcar")
st.write(f"A correlação entre o valor da produção de soja e o valor da produção de cama de açúcar é: {correlation:.2f}")

# Gráfico de Dispersão - Correlação entre Soja e Cama de Açúcar
st.subheader("Gráfico de Dispersão - Correlação entre Soja e Cama de Açúcar")
fig_scatter = px.scatter(merged_data, x='valor_soja', y='valor_cama', title="Correlação entre Soja e Cama de Açúcar", labels={'valor_soja': 'Valor da Produção de Soja (Mil Reais)', 'valor_cama': 'Valor da Produção de Cama de Açúcar (Mil Reais)'})
st.plotly_chart(fig_scatter)

# Análise de Potencial de Crescimento Futuro

# Calcular o crescimento médio anual (baseado na diferença do valor da produção entre os últimos dois anos)
df_soja_2['ano'] = pd.to_datetime(df_soja_2['periodos'], format='%Y').dt.year
soja_growth = df_soja_2['valor'].pct_change().mean()  # Crescimento médio percentual de soja

df_cama_2['ano'] = pd.to_datetime(df_cama_2['periodos'], format='%Y').dt.year
cama_growth = df_cama_2['valor'].pct_change().mean()  # Crescimento médio percentual de cama de açúcar

# Projetar para os próximos 5 anos
soja_future_values = [df_soja_2['valor'].iloc[-1] * (1 + soja_growth)**i for i in range(1, 6)]
cama_future_values = [df_cama_2['valor'].iloc[-1] * (1 + cama_growth)**i for i in range(1, 6)]

# Exibir os valores projetados
st.subheader("Projeção de Crescimento Futuro")
st.write("Projeção de crescimento da produção para os próximos 5 anos:")

# Mostrar os valores futuros
st.write(f"Projeção de Crescimento da Produção de Soja (milhões de Reais) nos próximos 5 anos: {soja_future_values}")
st.write(f"Projeção de Crescimento da Produção de Cama de Açúcar (milhões de Reais) nos próximos 5 anos: {cama_future_values}")

# Gráfico de Linha - Projeção de Crescimento Futuro
future_years = [2024 + i for i in range(1, 6)]
df_future = pd.DataFrame({
    'Ano': future_years,
    'Soja': soja_future_values,
    'Cama de Açúcar': cama_future_values
})

fig_future = px.line(df_future, x='Ano', y=['Soja', 'Cama de Açúcar'], title="Projeção de Crescimento Futuro", labels={'value': 'Valor (Milhões de Reais)', 'Ano': 'Ano'})
st.plotly_chart(fig_future)