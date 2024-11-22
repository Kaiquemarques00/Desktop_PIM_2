import flet as ft

from ..services.Api import Api
from ..componentes.popup import Popup

class Tabela:

    def __init__(self, page, checar_estado):
        self.page=page
        self.checar_estado=checar_estado


    def colunas(self, titulos):

        colunas=[]
        for titulo in titulos:
            colunas.append(
                ft.DataColumn(ft.Text(f"{titulo}", size=22, style=ft.TextStyle(color="#000000")))
            )

        return colunas
    
    def linhas(self, dados, caminho, caminho2):
        consultaAPI=Api(self.checar_estado).consulta(caminho)
        self.checar_estado.usuarios=consultaAPI
        popup=Popup(self.page, self.checar_estado)

        def expande_linha(e):
            id_linha=e.control.data
            consulta_por_id=Api(self.checar_estado).consulta_por_id(caminho2, id_linha)
            popup.show_popup_infos(consulta_por_id)

        linhas = []
        for dado in consultaAPI:
            linhas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(dado[dados[0]], size=20, style=ft.TextStyle(color="#000000"))),
                        ft.DataCell(ft.Text(dado[dados[1]], size=20, style=ft.TextStyle(color="#000000"))),
                        ft.DataCell(ft.Text(dado[dados[2]], size=20, style=ft.TextStyle(color="#000000"))),
                        ft.DataCell(ft.Text(dado[dados[3]], size=20, style=ft.TextStyle(color="#000000"))),
                        ],
                        selected=False,
                        data=dado[dados[0]],
                        on_select_changed=expande_linha,
                    )
                )
            
        return linhas

    def tabela(self, titulos, dados, caminho, caminho2):
        colunas=self.colunas(titulos)
        linhas=self.linhas(dados, caminho, caminho2)

        container_tabela = ft.Container(
            content=ft.DataTable(columns=colunas, rows=linhas, data_row_max_height=60, heading_row_height=60, column_spacing=120),
            alignment=ft.alignment.center,
            padding=50,
            expand=True
        )

        return container_tabela