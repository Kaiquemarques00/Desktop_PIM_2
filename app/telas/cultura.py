import flet as ft

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar
from ..componentes.tabela import Tabela
from ..componentes.botao_cadastra import BotaoFuncionalidade

class TelaCultura:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def cultura(self):
        appbar=Appbar(self.page).appBar()
        sidebar=Sidebar(self.page).sideBar("cultura")
        btn_cadastro=BotaoFuncionalidade(self.page, self.checar_estado).botaoCadastro("culture", "culturas")
        tabela=Tabela(self.page, self.checar_estado).tabela(["ID", "Nome", "Cultivo Dias", "Descrição"], ["cultura_id", "nome", "ciclo_cultivo_dias", "descricao"], "cultures", "culture")

        ###############################################################################
        ###############################################################################

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
                                    btn_cadastro
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