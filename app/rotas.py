import flet as ft

from app.telas.login import TelaLogin
from app.telas.home import TelaHome
from app.telas.usuarios import TelaUsuarios 
from app.telas.fornecedores import TelaFornecedores
from app.telas.cultura import TelaCultura


class ChecarEstado: # essa classe checa o estado do sistema para utilização do token de navegação
    def __init__(self):
        self.token=None
        self.dados_api=None

def registro_rotas(page:ft.Page):
    checar_estado=ChecarEstado()

    def mudar_rotas(route):

        page.views.clear() # limpa a tela

        #checagem de rotas
        if page.route=="/":
            obj_login=TelaLogin(page,checar_estado)
            page.views.append(ft.View(route="/",controls=[obj_login.login()]))

        elif page.route=="/home":
            obj_home=TelaHome(page,checar_estado)
            page.views.append(ft.View(route="/home",controls=[obj_home.home()]))
        
        elif page.route=="/usuarios":
            obj_usuarios=TelaUsuarios(page,checar_estado)
            page.views.append(ft.View(route="/usuarios",controls=[obj_usuarios.usuarios()]))

        elif page.route=="/fornecedores":
            obj_fornecedores=TelaFornecedores(page,checar_estado)
            page.views.append(ft.View(route="/fornecedores",controls=[obj_fornecedores.fornecedores()]))

        elif page.route=="/culturas":
            obj_cultura=TelaCultura(page,checar_estado)
            page.views.append(ft.View(route="/culturas",controls=[obj_cultura.cultura()]))


        page.update()

    page.on_route_change=mudar_rotas