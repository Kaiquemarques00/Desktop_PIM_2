import flet as ft

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar
from ..componentes.tabela import Tabela
from ..componentes.botao_cadastra import BotaoFuncionalidade

class TelaColheitas:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def colheitas(self):

        appbar=Appbar(self.page).appBar()
        sidebar=Sidebar(self.page).sideBar("colheitas")
        tabela=Tabela(self.page, self.checar_estado).tabela(["ID", "Plantio ID", "Data Colheita", "Quantidade"], ["colheita_id", "plantio_id", "data_colheita", "quantidade_colhida"], "harvests", "harvest", "colheitas", ["plantio_id", "qtd_colhida"])
        botoesFuncionalidade=BotaoFuncionalidade(self.page, self.checar_estado).botao_funcionalidade("harvest", "colheitas", ["plantio_id", "qtd_colhida"])
        
        ###############################################################################
        ###############################################################################

        btn_container=ft.Container(
            content=ft.Row(
                [
                    botoesFuncionalidade,
                ],
                alignment=ft.MainAxisAlignment.START,
                expand=True,
            ),
            padding=0,
            margin=ft.margin.only(left=140, bottom=100)
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
                            ft.Column(
                                [
                                    tabela,
                                    btn_container
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