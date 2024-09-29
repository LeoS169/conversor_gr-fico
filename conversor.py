import pandas as pd
import plotly.express as px


class Arquivo():

    def __init__(
            self,
            nome: str,
            endereco: str
    ):
        self.nome = nome
        self.endereco = endereco


    @property
    def get_endereco(self):
        return self.endereco
    

    @property
    def get_colunas_arq(self):
        
        arquivo = pd.read_csv(
            filepath_or_buffer=self.get_endereco
        )

        colunas = arquivo.columns
        return colunas
    
    
    def Testa_colunas(
            self,
            colunaX: str,
            colunaY: str
    ):
        colunas = self.get_colunas_arq
        
        if (colunaX not in colunas) or (colunaY not in colunas): #testa se as colunas estão no arquivo mesmo
            return False
        else:
            return True
        

    def cria_graifco(
            self,
            colunaX: str,
            colunaY: str
    ):
        arquivo = pd.read_csv(self.get_endereco)
        grafico = px.histogram(
            data_frame=arquivo,
            x=colunaX,
            y=colunaY
        )
        return grafico



