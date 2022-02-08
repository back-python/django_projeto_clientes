import re

def nome_valido(nome):
    return not bool(re.search(r'\d', nome))

def cpf_valido(cpf):
    cpf_regex = re.compile(r'(\d{3}\.?)(\d{3}\.?)(\d{3}\-?)(\d{2})')
    val = cpf_regex.search(cpf)
    
    if val != None:
        if len(val.group(0)) == 14:
            return cpf
        if len(val.group(0)) == 11:
            cpf = val.group(1) + '.' + val.group(2) + '.' + val.group(3) + '-' + val.group(4)
            return cpf
    return False

def celular_valido(celular):
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
    return len(rg) == 10
        