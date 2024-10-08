import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Função para coletar dados via web scraping (exemplo simplificado)
class ColetorDados:
    def __init__(self, url):
        self.url = url

    def coletar_dados(self):   
        dados = requests.get(self.url)
        if dados.status_code == 200:
            print("Dados coletados com sucesso.")
            print(dados.json())  # Verifique a estrutura dos dadosr
            return dados.json()
            
        else:
            print("Erro na coleta de dados.")
            return None


# Função para limpar os dados
class LimpezaDados:
    def __init__(self, dados):
        self.dados = dados

    def limpar_dados(self):
        df = pd.DataFrame(self.dados)
        print("Colunas disponíveis:", df.columns)
        df.dropna(inplace=True)  # Remove valores nulos

        # Renomear colunas, se necessário
        if 'original_coluna_x' in df.columns and 'original_coluna_y' in df.columns:
            df.rename(columns={'original_coluna_x': 'coluna_x', 'original_coluna_y': 'coluna_y'}, inplace=True)

        return df


# Função para gerar gráficos dos dados limpos
class VisualizarGrafico:
    def __init__(self, dados):
        completos = dados[dados['completed'] == True]
        incompletos = dados[dados['completed'] == False]

        # Contagem de completos e incompletos
        counts = [len(completos), len(incompletos)]
        labels = ['Completos', 'Incompletos']

        plt.figure(figsize=(10, 5))
        plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Distribuição de Tarefas Completas e Incompletas')
        plt.axis('equal')  # Assegura que o gráfico de pizza seja um círculo
        plt.show()

    # Função para treinar um modelo de Machine Learning simples (Regressão Linear)
class Treino:   
    def treinar_modelo(self, dados):
        X = dados[['coluna_x']]  # Feature
        y = dados['coluna_y']  # Target

        # Divisão dos dados em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Modelo de regressão linear
        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        # Avaliação do modelo
        y_pred = modelo.predict(X_test)
        erro = mean_squared_error(y_test, y_pred)
        print(f"Erro Quadrático Médio: {erro:.2f}")

    # Função principal que orquestra o pipeline de dados

def executar_pipeline(url):
    # Coletando dados
    dados_brutos = ColetorDados(url)

    if dados_brutos is not None:
        # Limpando dados
        dados_limpos = LimpezaDados(dados_brutos)

        # Gerando gráficos
        VisualizarGrafico(dados_limpos)

        # Treinando modelo
        Treino(dados_limpos)

    # URL de exemplo para coleta de dados
    url = "https://jsonplaceholder.typicode.com/todos"

    print(executar_pipeline(url))
