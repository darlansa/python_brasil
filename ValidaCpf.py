from validate_docbr import CPF

class Cpf:
    
    def __init__(self,documento) -> None:
        documento= str(documento)
        if self.cpfValid(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Invalido!!")
        
    def __str__(self) -> str:
        return self.formart_cpf()    
    
    def cpfValid(self, cpf):
        if len(cpf) == 11:
            validate = CPF()
            return validate.validate(cpf)
        else:
            raise ValueError("Quantidade de Digitos Invalida") 
    
    def formart_cpf(self):
        mask = CPF()
        return mask.mask(self.cpf)