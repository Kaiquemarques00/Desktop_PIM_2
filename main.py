import flet as ft

from app.rotas import registro_rotas #importa todas as rotas do sistema

def main(page:ft.Page):

    registro_rotas(page) # manda iniciar o registro de rotas
    page.title="Fazenda Horticultura"
    page.window.width=1280
    page.window.height=720
    page.window_min_width=1280
    page.window_min_height=720
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"

    page.go("/") # manda ir pra tela de login
    page.update # atualiza a tela

ft.app(target=main)