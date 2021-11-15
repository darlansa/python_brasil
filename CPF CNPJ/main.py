from ValidaCpfCnpj import Documento

# cpf = CpfCnpj("12345678900")
# print(cpf)

exemplo_cnpj = "11111111111"

documento = Documento.create_document(exemplo_cnpj)

print(documento)