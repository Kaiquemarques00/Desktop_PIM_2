import flet as ft

from ..componentes.popup import Popup

class BotaoFuncionalidade:

    def __init__(self, page, checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def botaoCadastro(self, caminho, tela, inputs_form):
        popup=Popup(self.page, self.checar_estado)

        def imprimir_funcionalidade(e):
            popup.show_popup_form(caminho, tela, inputs_form)
            

        btn_cadastra=ft.ElevatedButton(content=ft.Text("Cadastrar usuário", size=16), on_click=imprimir_funcionalidade, bgcolor="#1D3331", color=ft.colors.WHITE, height=40)

        btn_container=ft.Container(
            content=ft.Row(
                [
                    btn_cadastra
                ],
                alignment=ft.MainAxisAlignment.START,
                expand=True,
            ),
            padding=0,
            margin=ft.margin.only(left=140, bottom=100)
        )

        return btn_container