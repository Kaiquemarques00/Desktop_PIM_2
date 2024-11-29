import flet as ft

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar
from ..services.Api import Api

class TelaRelatorios:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def relatorios(self):
        consultaAPI=Api(self.checar_estado)
        appbar=Appbar(self.page).appBar()
        sidebar=Sidebar(self.page).sideBar("relatorios")
        
        ###############################################################################
        ###############################################################################
        vendaPeriodo=consultaAPI.vendaPeriodo()
        vendaCultura=consultaAPI.vendaCultura()
        vendaReceita=consultaAPI.vendaReceita()
        plantioPeriodo=consultaAPI.plantioPeriodo()
        plantioCulturas=consultaAPI.plantioCulturas()
        plantioStatus=consultaAPI.plantioStatus()
        colheitaPeriodo=consultaAPI.colheitaPeriodo()
        insumoFornecedor=consultaAPI.insumoFornecedor()

        print(insumoFornecedor)

        relatorio_1=ft.Container(
            width=400,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Venda último mês: ", color='#000000', size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Quantidade: {vendaPeriodo}", color='#000000', size=16),
                    ft.Text(f"Receita Total: {vendaReceita["receita_total"]["receita_total"]}", color='#000000', size=16),
                ]
            )
        )

        relatorio_2=ft.Container(
            width=400,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Culturas mais vendidas: ", color='#000000', size=18, weight=ft.FontWeight.BOLD),
                ]
            )
        )

        for venda in vendaCultura:
            venda_info = ft.Column([
                ft.Text(f"Cultura: {venda['cultura_nome']}", color='#000000', size=16),
                ft.Text(f"Quantidade: {venda['frequencia']}", color='#000000', size=16),
            ])

            relatorio_2.content.controls.append(venda_info)

        relatorio_3=ft.Container(
            width=400,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Plantios último mês: ", color='#000000', size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Quantidade: {plantioPeriodo}", color='#000000', size=16),
                    ft.Text(f"Culturas plantadas: ", color='#000000', size=18),
                ]
            )
        )

        for plantios in plantioCulturas:
            plantio_info = ft.Column([
                ft.Text(f"Cultura: {plantios['cultura_nome']}", color='#000000', size=16),
                ft.Text(f"Quantidade Plantada: {plantios['frequencia']}", color='#000000', size=16),
            ])

            relatorio_3.content.controls.append(plantio_info)

        header_status=ft.Text("Status dos plantios: ", color='#000000', size=18, weight=ft.FontWeight.BOLD)
        relatorio_3.content.controls.append(header_status)

        for status in plantioStatus:
            status_info = ft.Column([
                ft.Text(f"Status: {status['status']}", color='#000000', size=16),
                ft.Text(f"Quantidade: {status['frequencia']}", color='#000000', size=16),
            ])

            relatorio_3.content.controls.append(status_info)

        relatorio_4=ft.Container(
            width=400,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Colheitas último mês: ", color='#000000', size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Quantidade: {colheitaPeriodo}", color='#000000', size=16),
                ]
            )
        )

        relatorio_5=ft.Container(
            width=400,
            border=ft.border.only(
                top=ft.border.BorderSide(2,"black")),
            padding=15,
            content=ft.Column(
                [
                    ft.Text(f"Principais fornecedores: ", color='#000000', size=18, weight=ft.FontWeight.BOLD),
                ]
            )
        ) 

        for insumo in insumoFornecedor:
            insumo_info = ft.Column([
                ft.Text(f"Fornecedor: {insumo['fornecedor_nome']}", color='#000000', size=16),
                ft.Text(f"Quantidade de insumos: {insumo['frequencia']}", color='#000000', size=16),
            ])

            relatorio_5.content.controls.append(insumo_info)

        relatorios_container=ft.Container(
            width=400,
            bgcolor="#D9D9D9",
            margin=15,
            border=ft.border.all(5,ft.colors.BLACK),
            alignment=ft.alignment.center,
            content=ft.Column(
                [
                    relatorio_1,
                    relatorio_2,
                    relatorio_3,
                    relatorio_4,
                    relatorio_5
                ],
                expand=True,
                alignment=ft.alignment.center
            ),
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
                                    ft.Container(relatorios_container, expand=True, alignment=ft.alignment.center)
                                ],
                                expand=True,
                                alignment=ft.alignment.center,
                                scroll='auto'
                            )
                           # ft.Container(users,alignment=ft.alignment.center) # lista de usuários alinhada no centro da tela
                        ],
                        expand=True,
                        alignment=ft.alignment.center,
                        scroll='auto'
                    ),
                ],
                expand=True,
                alignment=ft.alignment.center,
                spacing=0,
            ),
            alignment=ft.alignment.center
        )

        return tela