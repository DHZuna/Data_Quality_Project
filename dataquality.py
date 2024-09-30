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
        display(HTML("<h3 style='font-size: 20px;'>Quick Info</h3>"))
        display(quick_info_df.style.set_table_attributes('style="font-size: 16px;"'))

    def firsts10(self):  # Primeiras 30 linhas
        head = self.dataframe.head(10)

        display(HTML("<h3 style='font-size: 20px;'>Previews</h3>"))
        display(HTML("<h2 style='font-size: 20px;'>Primeiras 10 Linhas</h2>"))
        display(head.style.set_table_attributes('style="font-size: 16px;"'))
