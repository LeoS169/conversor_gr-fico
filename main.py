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


def main(page: ft.Page): 
    page.title = 'Criador de gráfico'
    page.window_resizable = False

#Elementos a serem adicionados:
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
    
    
    def abre_graf():
        """
        Função do bot_abre_graf. Usa a função da classe Arquivo
        abre_graf() para abrir o gráfico no navegador.
        """
        arquivo = Arquivo(
            nome='arquivo_user',
            endereco=caminho_arquivo.value
        )

        arquivo.abre_graf(
            colunaX=entrada_eixoX.value,
            colunaY=entrada_eixoY.value
        )


    def testa_colunas():
        """
        Função do botão bot_testa_colunas. Irá validar as entradas
        do user para cada uma das colunas e, usando o método Testa_colunas,
        verifica se as colunas existem no arquivo. Habilita botão de abrir
        """
        arquivo = Arquivo(
            nome='arquivo_user',
            endereco=caminho_arquivo.value
        )

        if arquivo.endereco == '': # testa se o arquivo foi escolhido
            saida_usuário.value = 'Escolha um arquivo primeiro!'
        else: 
            if entrada_eixoX.value == '' or entrada_eixoY.value == '': #testa se há valores válidos nas entradas para as colunas
                saida_usuário.value = 'Ponha valores válidos de colunas!'
                bot_abre_graf.disabled = True
            else:
                teste_coluna = arquivo.Testa_colunas( 
                    colunaX=entrada_eixoX.value,
                    colunaY=entrada_eixoY.value
                )
                if teste_coluna == False:
                    saida_usuário.value = 'ERRO: alguma coluna (ou as duas) não existe no arquivo.'
                    bot_abre_graf.disabled = True
                else:
                    saida_usuário.value = 'Gráfico criado com sucesso!'
                    bot_abre_graf.disabled = False
        page.update()


    def pick_files_result(e: ft.FilePickerResultEvent):    
        """
        função de verificação do arquivo selecionado. Se o arquivo é selecionado
        o caminho dele é pego e alocado em caminho_arquivo.
        """
        if e.files: # testa se algum arquivo foi selecionado 
            caminho_arquivo.value = ",".join(map(lambda f: f.path, e.files))
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
                    )
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