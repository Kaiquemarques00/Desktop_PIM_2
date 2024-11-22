import flet as ft
import requests

API_URL="https://api-pim.onrender.com"

class Api:

    def __init__(self,checar_estado):
        self.checar_estado=checar_estado

    def consulta(self, endpoint):
        parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

        resultado=requests.get(f"{API_URL}/{endpoint}",headers=parametros)

        resposta_formatada=resultado.json()

        return resposta_formatada
    
    def consulta_arquivados(self, endpoint):
        parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

        resultado=requests.get(f"{API_URL}/{endpoint}/arc",headers=parametros)

        resposta_formatada=resultado.json()

        return resposta_formatada
    
    def consulta_por_id(self, endpoint, id):
        parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

        resultado=requests.get(f"{API_URL}/{endpoint}/{id}",headers=parametros)

        resposta_formatada=resultado.json()

        return resposta_formatada
    
    def consulta_arquivado_por_id(self, endpoint, id):
        parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

        resultado=requests.get(f"{API_URL}/{endpoint}/{id}/arc",headers=parametros)

        resposta_formatada=resultado.json()

        return resposta_formatada
    
    def cria(self, endpoint, dados):
        params = {
        "Authorization": f"Bearer {self.checar_estado.token}"
        }

        resposta = requests.post(f"{API_URL}/{endpoint}", headers=params, json=dados)

        respostaFormatada= resposta.json()

        return respostaFormatada
    
    def deleta(self, endpoint, id):
        params = {
        "Authorization": f"Bearer {self.checar_estado.token}"
        }

        resposta = requests.delete(f"{API_URL}/{endpoint}/{id}", headers=params)
        
        respostaFormatada= resposta.json()

        return respostaFormatada

    def altera_parcial(self, endpoint, id, dados):
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.patch(f"{API_URL}/{endpoint}/{id}", headers=params, json=dados)

            respostaFormatada= resposta.json()

            return respostaFormatada