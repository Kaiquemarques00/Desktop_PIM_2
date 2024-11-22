import flet as ft

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar
from ..componentes.tabela import Tabela
from ..componentes.botao_cadastra import BotaoFuncionalidade

class TelaFornecedores:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def fornecedores(self):
        appbar=Appbar(self.page).appBar()
        sidebar=Sidebar(self.page).sideBar("fornecedores")
        btn_cadastro=BotaoFuncionalidade(self.page, self.checar_estado).botaoCadastro("supplier", "fornecedores", ["nome", "cnpj", "email", "telefone", "rua", "numero", "bairro", "cidade", "estado", "cep"])
        tabela=Tabela(self.page, self.checar_estado).tabela(["ID", "CNPJ", "Nome", "Telefone"], ["fornecedor_id", "cnpj", "nome", "telefone"], "suppliers", "supplier")

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