import re
from validate_docbr import CPF, CNPJ

def validate_Documento(Documento):
    cpf = CPF()
    if len(Documento) != 11:
        return False
    return cpf.validate(Documento)

def validate_Nome(Nome):
    return  Nome.replace(" ", "").isalpha()

def validate_Email(Email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return (re.search(regex,Email))
    