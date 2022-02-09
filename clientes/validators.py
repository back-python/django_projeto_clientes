import re
from validate_docbr import CPF

def nome_valido(nome):
    """ Validando o nome """
    return not bool(re.search(r'\d', nome))

def cpf_valido(numero_cpf):
    """ Valida o CPF, com validate_docbr """
    cpf = CPF()
    if cpf.validate(numero_cpf):
        if len(numero_cpf) == 11:
            return cpf.mask(numero_cpf)
        elif len(numero_cpf) == 14:
            return numero_cpf
    return False

def celular_valido(celular):
    """ Valida o celular, utilizando expressões regulares """
    cel_regex = re.compile(r'\(?(\d{2})\)?(\d{5})\-?(\d{4})')
    val = cel_regex.search(celular)
    
    if val != None:
        if len(celular) == 14:
            return celular
        elif len(celular) == 11:
            celular = '(' + val.group(1) + ')' + val.group(2) + '-' + val.group(3)
            return celular
    return False

def rg_valido(rg):
    """ Verifica se o RG é valido """
    return len(rg) == 10
        