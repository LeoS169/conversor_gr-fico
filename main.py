"""
Aqui, ficará tudo relacionado ao aplicativo flet. Entrada e saída dos dados
O app terá que ter:

    -   [X]Abrir arquivo com tabelas (selecionar arquivo e o caminho dele ser guardado)
            --Envio do caminho para o conversor --

    -       Entrada para eixo y do gráfico (uma das colunas da tabela) [X]
                -> Entrada de texto para nome da coluna (testa se coluna existe no arquivo) / Seletor de colunas disponíveis <-
    -           entrada para exo x do gráfico [X]
                    -> Entrada de texto para nome da coluna (testa se coluna existe no arquivo) / Seletor de colunas disponíveis <-
    ]
            No def cria_gráfico -> testar os valores das entradas para cada eixo

    -               saída para o user: O gráfico com as possibilidades de download
"""
import flet as ft
from conversor import Arquivo


def main(page: ft.Page): # Criação de página inicial do app
    page.title = 'Criador de gráfico'

#Elementos:
    mensagem_ini = ft.Text(
        
        value='Gerador de gráficos',
        size=40
       
    )
    entrada_eixoX = ft.TextField(
        value='',
        label='Nome da coluna X'
    )

    entrada_eixoY = ft.TextField(
        value='',
        label='Nome da coluna Y'
    )

    bot_cria_graf = ft.ElevatedButton(
            text='Criar',
            on_click=lambda _:cria_graf()
    )


    def cria_graf():
        arquivo = Arquivo(
            nome='arquivo_user',
            endereco=caminho_arquivo.value
        )

        teste_coluna = arquivo.Testa_colunas( #será true se as douas colunas existirem
            colunaX=entrada_eixoX.value,
            colunaY=entrada_eixoY.value
        )
    


# Validação do arquivo:
    def pick_files_result(e: ft.FilePickerResultEvent):    
        if e.files: # testa se algum arquivo foi selecionado 

            caminho_arquivo.value = ",".join(map(lambda f: f.path, e.files))
            
            arquivo = Arquivo( # cria um objeto "Arquivo", com o nome e o endereco sendo o caminho pego usando o pick_file
                nome='arquivo_user',
                endereco=caminho_arquivo.value
            )

            print(arquivo.get_endereco) # teste para ver se tá pegando o endereco certo
            print(arquivo.get_colunas_arq[0]) # teste para ver se tá pegando as colunas
        else:

            caminho_arquivo.value = "Nenhum arquivo selecionado." 

        caminho_arquivo.update() # atualiza valores da variável de caminho_arquivo selecionados


    seletor_caminho_arquivo = ft.FilePicker(on_result=pick_files_result) # cria o seletor para selecão do arquivo
     # chama a função de verificação de caminho_arquivo, ao fim (para cancelar ou seleção do arquivo)

    page.overlay.append(seletor_caminho_arquivo) # adiciona o seletor sobre a página
    caminho_arquivo = ft.Text() # variável que aloca o caminho

# Adição dos elementos no app
    page.add(

        ft.Row(
            [

                mensagem_ini

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton( # botão no aplicativo para seleção
                    
                    "Selecionar Arquivo",
                    icon=ft.icons.FILE_OPEN_SHARP,
                    on_click=lambda _: seletor_caminho_arquivo.pick_files(
                        allow_multiple=False
                    ) #chama a função pick_files do seletor_caminho_arquivo,

                ),
                caminho_arquivo
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[

                entrada_eixoX,
                entrada_eixoY,
                bot_cria_graf

            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)