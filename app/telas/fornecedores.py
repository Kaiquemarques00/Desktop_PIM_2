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
        def ativa_tabela_arquivados(e):
            tabela.visible=False
            tabela_arquivados.visible=True
            btn_arquivados.content=ft.Text("Fornecedores ativos", size=16)
            btn_arquivados.on_click=ativa_tabela_ativos
            self.page.update()

        def ativa_tabela_ativos(e):
            tabela_arquivados.visible=False
            tabela.visible=True
            btn_arquivados.content=ft.Text("Fornecedores arquivados", size=16)
            btn_arquivados.on_click=ativa_tabela_arquivados
            self.page.update()

        appbar=Appbar(self.page).appBar()
        sidebar=Sidebar(self.page).sideBar("fornecedores")
        tabela=Tabela(self.page, self.checar_estado).tabela(["ID", "CNPJ", "Nome", "Telefone"], ["fornecedor_id", "cnpj", "nome", "telefone"], "suppliers", "supplier", "fornecedores", ["nome", "cnpj", "email", "telefone", "rua", "numero", "bairro", "cidade", "estado", "cep"])
        tabela_arquivados=Tabela(self.page, self.checar_estado).tabela_arquivado(["ID", "CNPJ", "Nome", "Telefone"], ["fornecedor_id", "cnpj", "nome", "telefone"], "suppliers", "supplier", "fornecedores", ["nome", "cnpj", "email", "telefone", "rua", "numero", "bairro", "cidade", "estado", "cep"])
        botoesFuncionalidade=BotaoFuncionalidade(self.page, self.checar_estado).botao_funcionalidade("supplier", "fornecedores", ["nome", "cnpj", "email", "telefone", "rua", "numero", "bairro", "cidade", "estado", "cep"])
        btn_arquivados=ft.ElevatedButton(content=ft.Text("Fornecedores arquivados", size=16), on_click=ativa_tabela_arquivados, bgcolor="#1D3331", color=ft.colors.WHITE, height=40)
        
        ###############################################################################
        ###############################################################################

        btn_container=ft.Container(
            padding=10,
            margin=10,
            content=ft.Row(
                [
                    botoesFuncionalidade,
                    btn_arquivados
                ],
                alignment=ft.MainAxisAlignment.START,
                expand=True,
            )
        )

        txt_tela=ft.Container(
            padding=10,
            margin=10,
            content=ft.Column(
                [
                    ft.Text("Gerenciamento de fornecedores",color=ft.colors.BLACK,size=20),
                    ft.Text(
                        "Aqui você pode visualizar e criar fornecedores.",
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
                                    tabela_arquivados,
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