from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def __str__(self):
        return self.formart_data()
        
    def mes_cadastro(self):
        mes_ano = [
             'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro','dezembro'
        ] 
        
        mes_cadastro= self.momento_cadastro.month-1
        return mes_ano[mes_cadastro]
    def dia_cadastro(self):
        dias_semana = [
            'segunda','terça','quarta','quinta','sexta','sábado','domingo'
            ] 
        dia_cadastro= self.momento_cadastro.weekday()
        return dias_semana[dia_cadastro]
        
    def formart_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M:%S')
        return data_formatada
        
    def tempo_cadatro(self):
        tempo_cadatro = datetime.today()- self.momento_cadastro
        return tempo_cadatro