from validate_docbr import CPF,CNPJ

class Documento:
    
    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Quantidade de Digitos Invalida")

class DocCpf:
    def __init__(self,document):
        if self.cpf_valid(document):
                self.cpf = document
        else:
            raise ValueError("CPF Invalido!!")
    
    def __str__(self):
        return self.formart_cpf()
    
    def cpf_valid(self, cpf):
        validate = CPF()
        return validate.validate(cpf)
        
    def formart_cpf(self):
        mask = CPF()
        return mask.mask(self.cpf)
    
class DocCnpj:
    def __init__(self,document):
        if self.cnpj_valid(document):
                self.cnpj = document
        else:
            raise ValueError("CNPJ Invalido!!")
    
    def __str__(self):
        return self.formart_cnpj()

    def cnpj_valid(self,cnpj):
        if len(cnpj) == 14:
            validate = CNPJ()
            return validate.validate(cnpj)
        else:
            raise ValueError("Quantidade de Digitos Invalida") 
        
    def formart_cnpj(self):
        mask = CNPJ()
        return mask.mask(self.cnpj) 
