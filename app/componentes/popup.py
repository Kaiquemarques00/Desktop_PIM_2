import flet as ft

from ..services.Api import Api
from ..componentes.formulario import Formulario

class Popup: 

    def __init__(self, page, checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def show_popup_form(self, caminho, tela, inputs_form):
        popup_form=self.popup_form(caminho, tela, inputs_form)
        self.page.dialog = popup_form
        popup_form.open = True
        self.page.update()

    def show_popup_infos(self, dados):
        popup_infos=self.popup_infos(dados)
        self.page.dialog = popup_infos
        popup_infos.open = True
        self.page.update()

    def popup_form(self, caminho, tela, inputs_form):
        formulario=Formulario(self.page, self.checar_estado).formulario(tela)
        
        def snack_feedback(e,mensagem):
            self.page.snack_bar=ft.SnackBar(
                ft.Text(
                    mensagem,
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#DA4E49"
            )
            self.page.snack_bar.open=True
            self.page.update()

        def manda_dados_form(e):
            inputs=formulario.content.controls
            self.checar_estado.dados_api = {inputs_form[i]: inputs[i].value for i in range(len(inputs))}
            dados_criacao=self.checar_estado.dados_api
            if "numero" in dados_criacao:
                dados_criacao["numero"] = int(dados_criacao["numero"])

            feedback = Api(self.checar_estado).cria(f"{caminho}", dados_criacao)
            snack_feedback(e, feedback)
            print(feedback)
            close_dialog(e)
            self.page.go("/home")
            self.page.go(f"/{tela}")
            self.page.update()



        def close_dialog(e):
            popup_cria.open = False
            
            self.page.update()


        popup_cria = ft.AlertDialog(
        title=ft.Container(ft.Text("Formulário Usuário"), alignment=ft.alignment.center, margin=ft.margin.only(bottom=50)),
        content=ft.Column([
            formulario
        ],
        scroll='auto',
        width=self.page.width * 0.95,
        alignment=ft.alignment.center
        ),
        actions=[
            ft.ElevatedButton("Cancelar", style=ft.ButtonStyle(bgcolor=ft.colors.RED, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=close_dialog),
            ft.ElevatedButton("Enviar", style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=manda_dados_form),
        ],
    )

        return popup_cria
    
    def popup_infos(self, dados):

        infos=[]
        for chave, valor in dados[0].items():
            infos.append(
                ft.TextField(label=f"{chave}" , value=f"{valor}", width=self.page.width * 0.8, read_only=True)
            )

        def close_dialog(e):
            popup_amplia.open = False
            self.page.update()

        

        def habilita_altera(e):
            for input in infos:
                input.read_only=False
                self.page.update()
                print(input)

        def altera(e):
            self.checar_estado.dados_api = {infos[i]: infos[i].value for i in range(len(infos))}
            dados_alteracao=self.checar_estado.dados_api
            
            print(dados_alteracao)
            #if "numero" in dados_criacao:
                #dados_criacao["numero"] = int(dados_criacao["numero"])

            #feedback = Api(self.checar_estado).cria(f"{caminho}", dados_criacao)
            #snack_feedback(e, feedback)
            #print(feedback)
            #close_dialog(e)
            #self.page.go("/home")
            #self.page.go(f"/{tela}")
            #self.page.update()


        popup_amplia = ft.AlertDialog(
        title=ft.Text("Dados"),
        content=ft.Column(infos,
        width=self.page.width * 0.95,
        scroll='auto',
        alignment=ft.alignment.center_right,
        ),
        actions=[
            ft.ElevatedButton("Cancelar", style=ft.ButtonStyle(bgcolor=ft.colors.RED, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=close_dialog),
            ft.ElevatedButton("Deletar", style=ft.ButtonStyle(bgcolor=ft.colors.RED, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=close_dialog),
            ft.ElevatedButton("Alterar", style=ft.ButtonStyle(bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=habilita_altera),
            ft.ElevatedButton("Enviar", style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=altera),
        ],
    )

        return popup_amplia