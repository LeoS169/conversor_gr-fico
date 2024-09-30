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
        """
        Só funciona para .csv, por enquanto
        """
        
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
        """
        Recebe entradas para colunas X e Y e testa
        se elas existem no arquivo selecionado
        return: True (se existirem)
        return: False (se não existirem)
        """
        colunas = self.get_colunas_arq
        
        if (colunaX not in colunas) or (colunaY not in colunas):
            return False
        else:
            return True
        

    def cria_grafico( 
            self,
            colunaX: str,
            colunaY: str
    ):
        """
        Recebe as colunas (já testadas) e cria o gráfico
        return: o gráfico criado
        """
        arquivo = pd.read_csv(self.get_endereco)
        grafico = px.histogram(
            data_frame=arquivo,
            x=colunaX,
            y=colunaY
        )
        return grafico
    

    def abre_graf(
            self,
            colunaX: str,
            colunaY: str
    ): 
        """
        Recebe as colunas (já testadas) e usa o cria_grafico
        para criar o gráfico de acordo com as colunas.
        Abre o gráfico no navegador
        """
        grafico = self.cria_grafico(
            colunaX=colunaX,
            colunaY=colunaY
        )
        grafico.show()



