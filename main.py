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
    page.window_resizable = False

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

    bot_testa_colunas = ft.ElevatedButton(
            text='Criar',
            on_click=lambda _:testa_colunas()
    )

    bot_abre_graf = ft.ElevatedButton(
        text='Abrir Gráfico',
        on_click=lambda _:abre_graf(),
        disabled=True
    )

    bot_salvar_graf = ft.ElevatedButton(
        text='Salvar Gráfico'
    )

    saida_usuário = ft.Text(value='Aqui aparecerá a mensagem para usuário')
    
    
#Funcção para criar grafico e abrir arquivo
    def abre_graf(): # abre o arquivo no formato html, no navegador

        arquivo = Arquivo(
            nome='arquivo_user',
            endereco=caminho_arquivo.value
        )

        arquivo.abre_graf(
            colunaX=entrada_eixoX.value,
            colunaY=entrada_eixoY.value
        )


# Testa valores de coluna
    def testa_colunas():

        arquivo = Arquivo(
            nome='arquivo_user',
            endereco=caminho_arquivo.value
        )

        if arquivo.endereco == '': # testa se o arquivo foi escolhido
            saida_usuário.value = 'Escolha um arquivo primeiro!'
        else: 
            if entrada_eixoX.value == '' or entrada_eixoY.value == '': #testa se há valores válidos nas entradas para as colunas
                saida_usuário.value = 'Ponha valores válidos de colunas!'
            else:
                teste_coluna = arquivo.Testa_colunas( #será true se as douas colunas existirem
                    colunaX=entrada_eixoX.value,
                    colunaY=entrada_eixoY.value
                )

                if teste_coluna == False:
                    saida_usuário.value = 'ERRO: alguma coluna (ou as duas) não existe no arquivo.'
                else:
                    saida_usuário.value = 'Gráfico criado com sucesso!'
                    bot_abre_graf.disabled = False
        page.update()


# Validação do arquivo:
    def pick_files_result(e: ft.FilePickerResultEvent):    

        if e.files: # testa se algum arquivo foi selecionado 
            caminho_arquivo.value = ",".join(map(lambda f: f.path, e.files))
            
            arquivo = Arquivo( # cria um objeto "Arquivo", com o nome e o endereco sendo o caminho pego usando o pick_file
                nome='arquivo_user',
                endereco=caminho_arquivo.value
            )
        else:
            caminho_arquivo.value = "Nenhum arquivo selecionado." 

        caminho_arquivo.update() # atualiza valores da variável de caminho_arquivo selecionados
        


    seletor_caminho_arquivo = ft.FilePicker(on_result=pick_files_result) # cria o seletor para selecão do arquivo
     # chama a função de verificação de caminho_arquivo, ao fim (para cancelar ou seleção do arquivo)

    page.overlay.append(seletor_caminho_arquivo) # adiciona o seletor sobre a página
    caminho_arquivo = ft.Text(value='') # variável que aloca o caminho


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
                bot_testa_colunas

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[

                saida_usuário,
                bot_abre_graf

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    
    )


ft.app(main)