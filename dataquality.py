import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Classe DataQuality para analisar datasets e gerar gráficos
class DataQuality: 
    def __init__(self, dataframe):
        self.dataframe = dataframe
 
    # Ver informações rápidas sobre a tabela:
    def quickinfo(self):
        # shape é um atributo, não um método
        shape = self.dataframe.shape       
        null_counts = self.dataframe.isnull().sum()       
        duplicated = self.dataframe.duplicated().sum()  # Corrigido: acesso direto ao dataframe

        print("Contagem de Linhas e Colunas (Linhas, Colunas):\n", shape)  # Contagem de linhas e colunas
        
        print("Contagem de valores nulos por coluna:\n", null_counts)  # Contagem de nulos
        print("Contagem de linhas duplicadas:\n", duplicated)  # Contagem de duplicados