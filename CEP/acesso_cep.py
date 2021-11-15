import requests

class BuscaEndereco:
    
    def __init__(self,cep):
        cep = str(cep)
        if self.cep_valid(cep):
            self.cep=cep
        else:
            raise ValueError("Cep Invalido")
            
    def __str__(self):
        return self.formart_cep()
        
    def cep_valid(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
        
    def formart_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
    
    def acessa_api(self):
        url= f"https://viacep.com.br/ws/{self.cep}/json"
        r = requests.get(url)
        dados = r.json()
        return (dados['uf'],
                dados['localidade'],
                dados['bairro'],
                dados['logradouro']
                )