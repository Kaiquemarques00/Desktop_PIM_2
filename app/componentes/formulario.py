import flet as ft

from ..services.Api import Api

class Formulario:

    def __init__(self, page, checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def form_usuarios(self):
        input_nome=ft.TextField(label="Nome: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_email=ft.TextField(label="E-mail: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_senha=ft.TextField(label="Senha: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE), password=True)
        input_role=ft.Dropdown(width=200, label="Tipo de usuário", label_style=ft.TextStyle(color=ft.colors.WHITE), color=ft.colors.WHITE, options=[ft.dropdown.Option("Administrador"), ft.dropdown.Option("Funcionario")])

        inputs=[input_nome, input_email, input_senha, input_role]

        return inputs
    
    def form_fornecedores(self):
        input_nome=ft.TextField(label="Nome: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_cnpj=ft.TextField(label="CNPJ: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_email=ft.TextField(label="E-mail: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_telefone=ft.TextField(label="Telefone: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_rua=ft.TextField(label="Rua: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_numero=ft.TextField(label="Número: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_bairro=ft.TextField(label="Bairro: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_cidade=ft.TextField(label="Cidade: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_estado=ft.TextField(label="Estado: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_cep=ft.TextField(label="CEP: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))


        inputs=[input_nome, input_cnpj, input_email, input_telefone, input_rua, input_numero, input_bairro, input_cidade, input_estado, input_cep]

        return inputs
    
    def form_culturas(self):
        input_nome=ft.TextField(label="Nome: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_ciclo=ft.TextField(label="Ciclo: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_descricao=ft.TextField(label="Descrição: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))


        inputs=[input_nome, input_ciclo, input_descricao]

        return inputs
    
    def formulario(self, tela):

        if tela == "usuarios":
            inputs=self.form_usuarios()
        elif tela == "fornecedores":
            inputs=self.form_fornecedores()
        elif tela == "culturas":
            inputs=self.form_culturas()
        

        formulario=ft.Container(
            content=ft.Column(
                inputs,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            ),
            alignment=ft.alignment.center,
            padding=0,
        )

        return formulario