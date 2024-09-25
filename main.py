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
            
        if e.files: #testa se algum arquivo foi selecionado

            arquivos.value = ','.join(map(lambda f: f.name, e.files))
                # função lambda irá receber um arquivo f e retornar sei nome (f.name), isso dentro de um map que irá
                # repetir a função para cada e.files, que aloca os arquivos
                # o join ira unir cada elemento da lista em um string, separado por uma ,
            
        else: 
            arquivos.value = "Nenhum arquivo selecionado." 

        arquivos.update() # atualiza valores da variável de arquivos selecionados

    seletor_arquivos = ft.FilePicker(on_result=pick_files_result) # cria o seletor para selecão de arquivos
    # chama a função de verificação de arquivos, ao fim

    page.overlay.append(seletor_arquivos) # adiciona o seletor sobre a página, quando necessário
    arquivos = ft.Text()

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