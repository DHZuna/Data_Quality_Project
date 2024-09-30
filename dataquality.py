import pandas as pd
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