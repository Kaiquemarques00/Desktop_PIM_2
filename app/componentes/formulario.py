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
    
    def form_insumos(self):
        consultaAPI=Api(self.checar_estado).consulta("suppliers")
        nome_fornecedores=[dicionario["nome"] for dicionario in consultaAPI]
        dropdown_opcoes = [
            ft.dropdown.Option(item) for item in nome_fornecedores
        ]

        input_nome=ft.TextField(label="Nome: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_tipo=ft.TextField(label="Tipo: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_medida=ft.TextField(label="Medida: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_quantidade=ft.TextField(label="Quantidade estoque: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_fornecedor=ft.Dropdown(width=200, label="Fornecedor: ", label_style=ft.TextStyle(color=ft.colors.WHITE), color=ft.colors.WHITE, options=dropdown_opcoes)
        input_observacoes=ft.TextField(label="Onservações: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))


        inputs=[input_nome, input_tipo, input_medida, input_quantidade, input_fornecedor, input_observacoes]

        return inputs
    
    def form_plantios(self):
        consultaAPI=Api(self.checar_estado).consulta("cultures")
        nome_culturas=[dicionario["nome"] for dicionario in consultaAPI]
        dropdown_opcoes = [
            ft.dropdown.Option(item) for item in nome_culturas
        ]

        input_cultura=ft.Dropdown(width=200, label="Cultura: ", label_style=ft.TextStyle(color=ft.colors.WHITE), color=ft.colors.WHITE, options=dropdown_opcoes)
        input_area=ft.TextField(label="Área plantada: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_status=ft.Dropdown(width=200, label="Status: ", label_style=ft.TextStyle(color=ft.colors.WHITE), color=ft.colors.WHITE, options=[ft.dropdown.Option("Planejado"), ft.dropdown.Option("Em andamento"), ft.dropdown.Option("Concluido"), ft.dropdown.Option("Cancelado")])
        input_insumos=ft.TextField(label="Lista insumo: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_observacoes=ft.TextField(label="Onservações: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))


        inputs=[input_cultura, input_area, input_status, input_insumos, input_observacoes]

        return inputs
    
    def form_colheitas(self):
        consultaAPI=Api(self.checar_estado).consulta("plantings")
        nome_culturas=[dicionario["plantio_id"] for dicionario in consultaAPI]
        dropdown_opcoes = [
            ft.dropdown.Option(item) for item in nome_culturas
        ]

        input_plantio_id=ft.Dropdown(width=200, label="Plantio: ", label_style=ft.TextStyle(color=ft.colors.WHITE), color=ft.colors.WHITE, options=dropdown_opcoes)
        input_quantidade=ft.TextField(label="Quantidade colhida: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))


        inputs=[input_plantio_id, input_quantidade]

        return inputs
    
    def form_pedidos(self):
        consultaAPI=Api(self.checar_estado).consulta("users")
        consultaAPI2=Api(self.checar_estado).consulta("cultures")
        id_usuarios=[dicionario["usuario_id"] for dicionario in consultaAPI]
        dropdown_opcoes = [
            ft.dropdown.Option(item) for item in id_usuarios
        ]
        nome_culturas=[dicionario["nome"] for dicionario in consultaAPI2]
        dropdown_opcoes_2 = [
            ft.dropdown.Option(item) for item in nome_culturas
        ]

        input_usuario_id=ft.Dropdown(width=200, label="Usuário ID: ", label_style=ft.TextStyle(color=ft.colors.WHITE), color=ft.colors.WHITE, options=dropdown_opcoes)
        input_cultura=ft.Dropdown(width=200, label="Cultura: ", label_style=ft.TextStyle(color=ft.colors.WHITE), color=ft.colors.WHITE, options=dropdown_opcoes_2)
        input_quantidade=ft.TextField(label="Quantidade: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_preco=ft.TextField(label="Preço: ", width=500, color=ft.colors.WHITE,label_style=ft.TextStyle(color=ft.colors.WHITE))
        input_status=ft.Dropdown(width=200, label="Status: ", label_style=ft.TextStyle(color=ft.colors.WHITE), color=ft.colors.WHITE, options=[ft.dropdown.Option("Pendente"), ft.dropdown.Option("Em andamento"), ft.dropdown.Option("Concluido")])


        inputs=[input_usuario_id, input_cultura, input_quantidade, input_preco, input_status]

        return inputs
    
    def formulario(self, tela):

        if tela == "usuarios":
            inputs=self.form_usuarios()
        elif tela == "fornecedores":
            inputs=self.form_fornecedores()
        elif tela == "culturas":
            inputs=self.form_culturas()
        elif tela == "insumos":
            inputs=self.form_insumos()
        elif tela == "plantios":
            inputs=self.form_plantios()
        elif tela == "colheitas":
            inputs=self.form_colheitas()
        elif tela == "pedidos":
            inputs=self.form_pedidos()

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