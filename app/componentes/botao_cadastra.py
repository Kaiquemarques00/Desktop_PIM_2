import flet as ft

from ..componentes.popup import Popup

class BotaoFuncionalidade:

    def __init__(self, page, checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def botao_funcionalidade(self, caminho2, tela, inputs_form):
        popup=Popup(self.page, self.checar_estado)

        def imprimir_funcionalidade(e):
            popup.show_popup_form(caminho2, tela, inputs_form)

        btn_cadastra=ft.ElevatedButton(content=ft.Text(f"Cadastrar {tela}", size=16), on_click=imprimir_funcionalidade, bgcolor="#1D3331", color=ft.colors.WHITE, height=40)

        return btn_cadastra