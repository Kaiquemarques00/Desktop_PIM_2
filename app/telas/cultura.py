import flet as ft

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar
from ..componentes.tabela import Tabela
from ..componentes.botao_cadastra import BotaoFuncionalidade

class TelaCultura:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def culturas(self):

        appbar=Appbar(self.page).appBar()
        sidebar=Sidebar(self.page).sideBar("culturas")
        tabela=Tabela(self.page, self.checar_estado).tabela(["ID", "Nome", "Cultivo Dias", "Descrição"], ["cultura_id", "nome", "ciclo_cultivo_dias", "descricao"], "cultures", "culture", "culturas", ["nome", "ciclo", "descricao"])
        botoesFuncionalidade=BotaoFuncionalidade(self.page, self.checar_estado).botao_funcionalidade("culture", "culturas", ["nome", "ciclo", "descricao"])
        
        ###############################################################################
        ###############################################################################

        btn_container=ft.Container(
            padding=10,
            margin=10,
            content=ft.Row(
                [
                    botoesFuncionalidade,
                ],
                alignment=ft.MainAxisAlignment.START,
                expand=True,
            ),
        )

        txt_tela=ft.Container(
            padding=10,
            margin=10,
            content=ft.Column(
                [
                    ft.Text("Gerenciamento de Culturas",color=ft.colors.BLACK,size=20),
                    ft.Text(
                        "Aqui você pode visualizar e criar culturas.",
                        color=ft.colors.BLACK
                    )
                ]
            )
        )

        tela=ft.Container(
            expand=True,
            bgcolor="#D9D9D9",
            content=ft.Row(
                [
                    sidebar,
                    ft.Column(
                        [
                            appbar,
                            ft.Row(
                                [
                                    txt_tela,
                                    btn_container
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            ft.Column(
                                [
                                    tabela,
                                ],
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                scroll='auto'
                            ),
                           # ft.Container(users,alignment=ft.alignment.center) # lista de usuários alinhada no centro da tela
                        ],
                        expand=True,
                        alignment=ft.alignment.center
                    ),
                ],
                expand=True,
                alignment=ft.alignment.center,
                spacing=0,
            ),
            alignment=ft.alignment.center
        )

        return tela