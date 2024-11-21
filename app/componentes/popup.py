import flet as ft

from ..services.Api import Api

class Popup:

    def __init__(self, page, checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def show_popup_form(self, dados, caminho, tela):
        popup_form=self.popup_form(dados, caminho, tela)
        self.page.dialog = popup_form
        popup_form.open = True
        self.page.update()

    def show_popup_infos(self, dados):
        popup_infos=self.popup_infos(dados)
        self.page.dialog = popup_infos
        popup_infos.open = True
        self.page.update()

    def popup_form(self, dados, caminho, tela):
        dados_criacao={}
        infos=[]
        for chave, valor in dados[0].items():
            infos.append(
                ft.TextField(label=f"{chave}", width=self.page.width * 0.8)
            )

        def manda_dados_api(e):
            for info in infos:
                dados_criacao[info.label] = info.value

            del dados_criacao["cultura_id"]
            dados_criacao['ciclo'] = dados_criacao.pop('ciclo_cultivo_dias')
            dados_criacao["ciclo"] = int(dados_criacao["ciclo"])
            print(type(dados_criacao["ciclo"]))

            feedback = Api(self.checar_estado).cria(f"{caminho}", dados_criacao)
            infos.append(ft.Text(feedback))
            print(dados_criacao)
            print(feedback)
            close_dialog(e)
            self.page.go("/home")
            self.page.go(f"/{tela}")
            self.page.update()



        def close_dialog(e):
            popup_cria.open = False
            
            self.page.update()


        popup_cria = ft.AlertDialog(
        title=ft.Text("Formulário"),
        content=ft.Column(infos,
        width=self.page.width * 0.95,
        alignment=ft.alignment.center_right
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=close_dialog),
            ft.TextButton("Enviar", on_click=manda_dados_api),
        ],
    )

        return popup_cria
    
    def popup_infos(self, dados):

        infos=[]
        for chave, valor in dados[0].items():
            infos.append(
                ft.TextField(label=f"{chave}" , value=f"{valor}", width=self.page.width * 0.8)
            )

        def close_dialog(e):
            popup_amplia.open = False
            self.page.update()


        popup_amplia = ft.AlertDialog(
        title=ft.Text("Dados"),
        content=ft.Column([ft.TextField(label=f"{chave}" , value=f"{valor}", width=self.page.width * 0.8, read_only=True) for chave, valor in dados[0].items()],
        width=self.page.width * 0.95,
        alignment=ft.alignment.center_right
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=close_dialog),
        ],
    )

        return popup_amplia