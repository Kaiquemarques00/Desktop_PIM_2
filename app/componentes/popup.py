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

    def show_popup_infos(self, dados, tela, inputs_form, caminho2):
        popup_infos=self.popup_infos(dados, tela, inputs_form, caminho2)
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
            print(inputs)
            self.checar_estado.dados_api = {inputs_form[i]: inputs[i].value for i in range(len(inputs))}
            dados_criacao=self.checar_estado.dados_api
            if "numero" in dados_criacao:
                dados_criacao["numero"] = int(dados_criacao["numero"])
            if "ciclo" in dados_criacao:
                dados_criacao["ciclo"] = int(dados_criacao["ciclo"])
            if "area_plantada" in dados_criacao:
                dados_criacao["area_plantada"] = float(dados_criacao["area_plantada"])
            if "qtd_estoque" in dados_criacao:
                dados_criacao["qtd_estoque"] = float(dados_criacao["qtd_estoque"])
            if "custo_por_unidade" in dados_criacao:
                dados_criacao["custo_por_unidade"] = float(dados_criacao["custo_por_unidade"])
            if "plantio_id" in dados_criacao:
                dados_criacao["plantio_id"] = int(dados_criacao["plantio_id"])
            if "qtd_colhida" in dados_criacao:
                dados_criacao["qtd_colhida"] = float(dados_criacao["qtd_colhida"])
            if "usuario_id" in dados_criacao:
                dados_criacao["usuario_id"] = int(dados_criacao["usuario_id"])
            if "quantidade" in dados_criacao:
                dados_criacao["quantidade"] = int(dados_criacao["quantidade"])
            if "preco_unitario" in dados_criacao:
                dados_criacao["preco_unitario"] = float(dados_criacao["preco_unitario"])

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
    
    def popup_infos(self, dados, tela, inputs_form, caminho2):
        formulario=Formulario(self.page, self.checar_estado).formulario(tela)

        infos=[]
        for chave, valor in dados[0].items():
            infos.append(
                ft.TextField(label=f"{chave}" , value=f"{valor}", width=self.page.width * 0.8, read_only=True)
            )

        def close_dialog(e):
            popup_amplia.open = False
            self.page.update()

        def deleta_arquiva(e):
            campo, id = list(dados[0].items())[0]
            feedback = Api(self.checar_estado).deleta(f"{caminho2}", id)
            snack_feedback(e, feedback)
            print(feedback)
            close_dialog(e)
            self.page.go("/home")
            self.page.go(f"/{tela}")
            self.page.update()

        alerta_deleta=ft.AlertDialog(
            modal=True,
            bgcolor="#2A383E",
            title=ft.Text("CONFIRMAR DELEÇÃO/ARQUIVAÇÃO"),
            content=ft.Text("Você realmente deseja prosseguir com a deleção/arquivação ?"),
            actions=[
                ft.TextButton("Sim", on_click=deleta_arquiva),
                ft.TextButton("Não", on_click=lambda e:self.page.close(alerta_deleta)),
            ]
        )

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

        def habilita_altera(e):
            popup_amplia.content = formulario
            popup_amplia.content. width = self.page.width * 0.95
            inputs=formulario.content.controls
            values=[]
            for valor in list(dados[0].values())[1: len(list(dados[0]))]:
                values.append(valor)
            i=0
            for input in inputs:
                input.value = values[i]
                i = i + 1
                if(input.label=="Senha: "):
                    input.value = None
            self.page.update()

        def altera(e):
            inputs=formulario.content.controls
            dados_verifica = {inputs_form[i]: inputs[i].value for i in range(len(inputs))}
            dados_inputs=dados[0]
            dados_formatados = {novo: dados_inputs[antigo] for antigo, novo in zip(dados_inputs.keys(), dados_verifica.keys())}
            print(dados_formatados)
            print(dados_verifica)
            dados_alteracao={}
            for chave in dados_inputs:
                if chave in dados_verifica and dados_inputs[chave] != dados_verifica[chave]:
                # Se os valores forem diferentes, adiciona no novo dicionário
                    dados_alteracao[chave] = (dados_verifica[chave])

            campo, id = list(dados[0].items())[0]
            if "numero" in dados_alteracao:
                dados_alteracao["numero"] = int(dados_alteracao["numero"])
            print(dados_alteracao)
            feedback = Api(self.checar_estado).altera_parcial(f"{caminho2}", id, dados_alteracao)
            snack_feedback(e, feedback)
            print(feedback)
            close_dialog(e)
            self.page.go("/home")
            self.page.go(f"/{tela}")
            self.page.update()


        popup_amplia = ft.AlertDialog(
        title=ft.Text("Dados"),
        content=ft.Column(infos,
        width=self.page.width * 0.95,
        scroll='auto',
        alignment=ft.alignment.center_right,
        ),
        actions=[
            ft.ElevatedButton("Cancelar", style=ft.ButtonStyle(bgcolor=ft.colors.RED, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=close_dialog),
            ft.ElevatedButton("Deletar", style=ft.ButtonStyle(bgcolor=ft.colors.RED, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=lambda e:self.page.open(alerta_deleta)),
            ft.ElevatedButton("Alterar", style=ft.ButtonStyle(bgcolor=ft.colors.BLUE, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=habilita_altera),
            ft.ElevatedButton("Enviar", style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=16)), height=40, on_click=altera),
        ],
    )

        return popup_amplia