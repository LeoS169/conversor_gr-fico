"""
Aqui, ficará tudo relacionado ao aplicativo flet. Entrada e saída dos dados
O app terá que ter:

    -   Abrir arquivo com tabelas
    -       Entrada para eixo y do gráfico (uma das colunas da tabela)
    -           entrada para exo x do gráfico
    -               saída para o user: O gráfico com as possibilidades de download
"""
import flet as ft

def main(page: ft.Page): # Criação de página inicial do app

    def pick_files_result(e: ft.FilePickerResultEvent): # função para a seleção de arquivos. e contém as informações de selceçãp

        arquivos.value = ( # variável com os arquivos selcecionados
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!" # se arquivos forem selecionados (if e.files)
            # executa-se a parte de trás. Que percorre cada arquivo (f) da lista (e.files) pegando seu nome e unindo em uma só string.
            # map(lambda f: f.name, e.files) pega gada nome de arquivo e põe na lista
            # ','.join() separa os valores por uma virgula
        )

        arquivos.update() # atualiza valores da variável de arquivos selecionados

    seletor_arquivos = ft.FilePicker(on_result=pick_files_result) # cria o seletor para selecão de arquivos
    # chama a função de verificação de arquivos, ao fim

    arquivos = ft.Text()

    page.overlay.append(seletor_arquivos) # adiciona o seletor sobre a página, quando necessário

    page.add(

        ft.Row(
            [
                ft.ElevatedButton( # botão no aplicativo para seleção
                    
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: seletor_arquivos.pick_files( #chama a função pick_files do seletor_arquivos
                        allow_multiple=True
                    ),

                ),

                arquivos,
            ]
        )
    )

ft.app(main)