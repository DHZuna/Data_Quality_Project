import pandas as pd
from IPython.display import display, HTML

# Classe DataQuality para analisar datasets e gerar gráficos
class DataQuality: 
    def __init__(self, dataframe):
        self.dataframe = dataframe
 
    # Ver informações rápidas sobre a tabela:
    def quickinfo(self):
        shape = self.dataframe.shape       
        null_counts = self.dataframe.isnull().sum()       
        duplicated = self.dataframe.duplicated().sum()  

        #Criar dataframe unificado
        quick_info_df = pd.DataFrame({ 

            "Descrição" : ["Linhas", "Colunas", "Valores Nulos", "Linhas Duplicadas"],
            "Contagem" : [ 
                shape[0],
                shape[1],
                null_counts[null_counts > 0].sum(),
                duplicated
             ]
        })

# Aumentar a fonte e exibir a tabela
        display(HTML("<h3 style='font-size: 20px;'>Quick Info</h3>"))
        display(quick_info_df.style.set_table_attributes('style="font-size: 16px;"'))
