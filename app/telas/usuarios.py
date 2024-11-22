import flet as ft

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar
from ..componentes.tabela import Tabela
from ..componentes.botao_cadastra import BotaoFuncionalidade

class TelaUsuarios:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def usuarios(self):
        appbar=Appbar(self.page).appBar()
        sidebar=Sidebar(self.page).sideBar("usuarios")
        btn_cadastro=BotaoFuncionalidade(self.page, self.checar_estado).botaoCadastro("user", "usuarios", ["nome", "email", "senha", "role"])
        tabela=Tabela(self.page, self.checar_estado).tabela(["ID", "Nome", "Email", "Cargo"], ["usuario_id", "nome", "email", "tipo_usuario"], "users", "user", "usuarios", ["nome", "email", "senha", "role"])

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