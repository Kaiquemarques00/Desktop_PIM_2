import flet as ft

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar

class TelaHome:

    def __init__(self,page,checar_estado):
        self.page=page
        self.app_state=checar_estado

    def home(self):
        appbar = Appbar(self.page).appBar()
        sidebar = Sidebar(self.page).sideBar("home")

        txt_tela=ft.Container(
            padding=10,
            margin=10,
            content=ft.Column(
                [
                    ft.Text("Bem-vindo ao Sistema de Gerenciamento da Fazenda Urbana",color=ft.colors.BLACK,size=20),
                    ft.Text(
                        "Aqui você pode visualizar um resumo das operações.\nNavegue pelas opções do menu para gerenciar as culturas, plantios, colheitas e mais",
                        color=ft.colors.BLACK
                    )
                ]
            )
        )

        tela = ft.Container(
            expand=True,
            bgcolor="#D9D9D9",
            content=ft.Row(
                [
                    sidebar,
                    ft.Column(
                        [
                            appbar,
                            txt_tela
                        ],
                        expand=True
                    )
                ],
                spacing=0
            )
        )

        return tela