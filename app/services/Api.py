import flet as ft
import requests

API_URL="https://api-pim.onrender.com"

class Api:

    def __init__(self,checar_estado):
        self.checar_estado=checar_estado

    def consulta(self, endpoint):
        try:
            parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

            resultado=requests.get(f"{API_URL}/{endpoint}",headers=parametros)

            resposta_formatada=resultado.json()

            return resposta_formatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)
    
    def consulta_arquivados(self, endpoint):
        try:
            parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

            resultado=requests.get(f"{API_URL}/{endpoint}/arc",headers=parametros)

            resposta_formatada=resultado.json()

            return resposta_formatada
            
        except requests.exceptions.RequestException as ex:
            print(ex)
    
    def consulta_por_id(self, endpoint, id):
        try: 
            parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

            resultado=requests.get(f"{API_URL}/{endpoint}/{id}",headers=parametros)

            resposta_formatada=resultado.json()

            return resposta_formatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)
    
    def consulta_arquivado_por_id(self, endpoint, id):
        try:
            parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

            resultado=requests.get(f"{API_URL}/{endpoint}/{id}/arc",headers=parametros)

            resposta_formatada=resultado.json()

            return resposta_formatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)
    
    def cria(self, endpoint, dados):
        try:
            params = {
                "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.post(f"{API_URL}/{endpoint}", headers=params, json=dados)

            respostaFormatada= resposta.json()

            return respostaFormatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)
    
    def deleta(self, endpoint, id):
        try:
            params = {
                "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.delete(f"{API_URL}/{endpoint}/{id}", headers=params)
            
            respostaFormatada= resposta.json()

            return respostaFormatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)

    def altera_parcial(self, endpoint, id, dados):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.patch(f"{API_URL}/{endpoint}/{id}", headers=params, json=dados)

            respostaFormatada= resposta.json()

            return respostaFormatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)

    # Relatorios

    def vendaPeriodo(self):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.get(f"{API_URL}/report/sale/period?mesI=10&mesF=12", headers=params)

            respostaFormatada= resposta.json()

            return respostaFormatada
        
            
        
        except requests.exceptions.RequestException as ex:
            print(ex)

    def vendaCultura(self):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.get(f"{API_URL}/report/sale/culture", headers=params)

            respostaFormatada= resposta.json()

            return respostaFormatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)

    def vendaReceita(self):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.get(f"{API_URL}/report/sale/revenue", headers=params)

            respostaFormatada= resposta.json()

            return respostaFormatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)

    def plantioPeriodo(self):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.get(f"{API_URL}/report/plantings/period?mesI=10&mesF=12", headers=params)

            respostaFormatada= resposta.json()

            return respostaFormatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)

    def plantioCulturas(self):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.get(f"{API_URL}/report/plantings/cultures", headers=params)

            respostaFormatada= resposta.json()

            return respostaFormatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)

    def plantioStatus(self):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.get(f"{API_URL}/report/plantings/status", headers=params)

            respostaFormatada= resposta.json()

            return respostaFormatada
        
        except requests.exceptions.RequestException as ex:
            print(ex)

    def colheitaPeriodo(self):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.get(f"{API_URL}/report/harvest/period?mesI=10&mesF=12", headers=params)

            respostaFormatada= resposta.json()

            return respostaFormatada
            
        except requests.exceptions.RequestException as ex:
            print(ex)

    def insumoFornecedor(self):
        try:
            params = {
            "Authorization": f"Bearer {self.checar_estado.token}"
            }

            resposta = requests.get(f"{API_URL}/report/inputs/suppliers", headers=params)

            respostaFormatada= resposta.json()

            return respostaFormatada
            
        except requests.exceptions.RequestException as ex:
            print(ex)

            