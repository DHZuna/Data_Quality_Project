import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, HTML

# Classe DataQuality para analisar datasets e gerar gráficos
class DataQuality: 
    def __init__(self, dataframe):
        self.dataframe = dataframe
 
    def quickinfo(self):  # Quick Info
        shape = self.dataframe.shape       
        null_counts = self.dataframe.isnull().sum()       
        duplicated = self.dataframe.duplicated().sum()  

        # Dataframe unificado
        quick_info_df = pd.DataFrame({ 
            "Descrição" : ["Linhas", "Colunas", "Valores Nulos", "Linhas Duplicadas"],
            "Contagem" : [ 
                shape[0],
                shape[1],
                null_counts[null_counts > 0].sum(),
                duplicated
             ]
        })
        # Fonte maior e tabela
        display(HTML("<h2 style='font-size: 20px;'>Quick Info</h2>"))
        display(quick_info_df.style.set_table_attributes('style="font-size: 16px;"'))

    def datatypes(self):  # Inferred Data Types
        # Mapear os tipos de dados inferidos
        inferred_types = []
        for col in self.dataframe.columns:
            if self.dataframe[col].dtype == 'object':
                unique_values = self.dataframe[col].nunique()
                if unique_values == len(self.dataframe):
                    inferred_types.append('unique')
                else:
                    inferred_types.append('categorical')
            elif pd.api.types.is_numeric_dtype(self.dataframe[col]):
                inferred_types.append('numeric')
            elif pd.api.types.is_bool_dtype(self.dataframe[col]):
                inferred_types.append('boolean')
            else:
                inferred_types.append('categorical')

        # Criar dataframe com o nome das colunas e seus tipos inferidos
        datatypes_df = pd.DataFrame({
            "Nome da Coluna": self.dataframe.columns,
            "Tipo Inferido": inferred_types
        })
        
        # Exibir a tabela com fonte maior
        display(HTML("<h2 style='font-size: 20px;'>Data Types</h2>"))
        display(datatypes_df.style.set_table_attributes('style="font-size: 16px;"'))

    def firsts10(self):  # Primeiras 30 linhas
        head = self.dataframe.head(10)

        display(HTML("<h2 style='font-size: 20px;'>Data Preview</h2>"))
        display(HTML("<h3 style='font-size: 20px;'>As 10 primeiras linhas: </h3>"))
        display(head.style.set_table_attributes('style="font-size: 16px;"'))

    def missing_values(self):  # Missing Values Table and Plot
        # Contar valores nulos e calcular o percentual
        null_counts = self.dataframe.isnull().sum()
        null_percentage = (null_counts / len(self.dataframe)) * 100

        # Criar dataframe com valores nulos e percentuais
        missing_values_df = pd.DataFrame({
            "Nome da Coluna": self.dataframe.columns,
            "Contagem de Nulos": null_counts,
            "Percentual de Nulos (%)": null_percentage
        }).sort_values(by="Contagem de Nulos", ascending=False)

        # Exibir tabela de valores nulos com formatação
        display(HTML("<h3 style='font-size: 20px;'>Valores nulos</h3>"))
        display(missing_values_df.style.set_table_attributes('style="font-size: 16px;"'))

        # Gerar gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.barh(missing_values_df["Nome da Coluna"], missing_values_df["Contagem de Nulos"], color='skyblue')
        plt.xlabel('Contagem de Nulos')
        plt.title('Valores Nulos por Coluna')
        plt.gca().invert_yaxis()  # Inverter eixo y para facilitar leitura
        plt.show()


    def unique_values(self):  # Unique Values Table and Plot
        unique_counts = self.dataframe.nunique()

        # Criar dataframe com contagem de valores únicos
        unique_values_df = pd.DataFrame({
            "Nome da Coluna": self.dataframe.columns,
            "Valores Únicos": unique_counts
        }).sort_values(by="Valores Únicos", ascending=False)

        display(HTML("<h3 style='font-size: 20px;'>Valores Unicos</h3>"))
        display(unique_values_df.style.set_table_attributes('style="font-size: 16px;"'))

        # Gerar gráfico de barras para valores únicos
        plt.figure(figsize=(10, 6))
        plt.barh(unique_values_df["Nome da Coluna"], unique_values_df["Valores Únicos"], color='lightgreen')
        plt.xlabel('Contagem de Valores Únicos')
        plt.title('Valores Únicos por Coluna')
        plt.gca().invert_yaxis()  # Inverter eixo y para melhor visualização
        plt.show()

    
       # Método para contar os valores em colunas categóricas
    def categorical_value_counts(self): 
        categorical_columns = self.dataframe.select_dtypes(include=['object']).columns
        display(HTML("<h3 style='font-size: 20px;'>Contagens de valor em colunas categóricas</h3>"))

        # Loop through each categorical column
        for col in categorical_columns:
            display(HTML(f"<h4 style='font-size: 18px;'>{col} - Contagem de Valores</h4>"))
            
            # Contagem dos valores em cada categoria
            value_counts_df = self.dataframe[col].value_counts().reset_index()
            value_counts_df.columns = [col, 'Contagem']
            display(value_counts_df.style.set_table_attributes('style="font-size: 16px;"'))
            
            # Gerar gráfico de barras para visualização
            plt.figure(figsize=(10, 6))
            plt.barh(value_counts_df[col], value_counts_df['Contagem'], color='lightcoral')
            plt.xlabel('Contagem')
            plt.title(f'Contagem de {col}')
            plt.gca().invert_yaxis()  # Inverter eixo y para melhor visualização
            plt.show()

       # Método para exibir estatísticas descritivas das colunas numéricas
    def describe_numeric(self):
        numeric_columns = self.dataframe.select_dtypes(include=['number']).columns
        display(HTML("<h3 style='font-size: 20px;'>Estatísticas Descritivas das Colunas Numéricas</h3>"))
        
        # Calcular estatísticas descritivas para colunas numéricas
        desc_df = self.dataframe[numeric_columns].describe().T  # Transpor para uma visualização melhor
        desc_df['count'] = desc_df['count'].astype(int)  # Formatar contagem como inteiro

        # Exibir tabela de estatísticas descritivas
        display(desc_df.style.set_table_attributes('style="font-size: 16px;"'))
        
        # Gerar gráficos de distribuição (histogramas) para cada coluna numérica
        for col in numeric_columns:
            plt.figure(figsize=(10, 6))
            plt.hist(self.dataframe[col].dropna(), bins=15, color='skyblue', edgecolor='black')
            plt.title(f'Distribuição de {col}')
            plt.xlabel(col)
            plt.ylabel('Frequência')
            plt.grid(True)
            plt.show()