from acesso_cep import BuscaEndereco

cep = "53990970"
obj_cep = BuscaEndereco(cep)

estado,cidade,bairro,logradouro = obj_cep.acessa_api()

retorno = obj_cep.acessa_api()

for texto in retorno:
    print(texto)