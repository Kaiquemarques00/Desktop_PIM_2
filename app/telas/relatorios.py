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
            content=ft.Column(
                [
                    ft.Text(f"Venda último mês: ", color='#000000'),
                    ft.Text(f"Quantidade: {vendaPeriodo}", color='#000000'),
                    ft.Text(f"Receita Total: {vendaReceita["receita_total"]["receita_total"]}", color='#000000'),
                ]
            )
        )

        relatorio_2=ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Culturas mais vendidas: ", color='#000000'),
                ]
            )
        )

        for venda in vendaCultura:
            venda_info = ft.Column([
                ft.Text(f"Cultura: {venda['cultura_nome']}", color='#000000'),
                ft.Text(f"Quantidade: {venda['frequencia']}", color='#000000'),
            ])

            relatorio_2.content.controls.append(venda_info)

        relatorio_3=ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Plantios último mês: ", color='#000000'),
                    ft.Text(f"Quantidade: {plantioPeriodo}", color='#000000'),
                    ft.Text(f"Culturas plantadas: ", color='#000000'),
                ]
            )
        )

        for plantios in plantioCulturas:
            plantio_info = ft.Column([
                ft.Text(f"Cultura: {plantios['cultura_nome']}", color='#000000'),
                ft.Text(f"Quantidade Plantada: {plantios['frequencia']}", color='#000000'),
            ])

            relatorio_3.content.controls.append(plantio_info)

        relatorio_3.content.controls.append(ft.Text("Status dos plantios: ", color='#000000'))

        for status in plantioStatus:
            status_info = ft.Column([
                ft.Text(f"Status: {status['status']}", color='#000000'),
                ft.Text(f"Quantidade: {status['frequencia']}", color='#000000'),
            ])

            relatorio_3.content.controls.append(status_info)

        relatorio_4=ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Colheitas último mês: ", color='#000000'),
                    ft.Text(f"Quantidade: {colheitaPeriodo}", color='#000000'),
                ]
            )
        )

        relatorio_5=ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Colheitas último mês: ", color='#000000'),
                    ft.Text(f"Quantidade: {colheitaPeriodo}", color='#000000'),
                ]
            )
        ) 

        for insumo in insumoFornecedor:
            insumo_info = ft.Column([
                ft.Text(f"Fornecedor: {insumo['fornecedor_nome']}", color='#000000'),
                ft.Text(f"Quantidade de insumos: {insumo['frequencia']}", color='#000000'),
            ])

            relatorio_5.content.controls.append(insumo_info)

        relatorios_container=ft.Container(
            content=ft.Row(
                [
                    relatorio_1,
                    relatorio_2,
                    relatorio_3,
                    relatorio_4,
                    relatorio_5
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
                                    relatorios_container
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