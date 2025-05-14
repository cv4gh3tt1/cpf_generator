import random

def calcular_digito_verificador(numeros):
    """Calcula um dígito verificador do CPF."""
    soma = 0
    peso = len(numeros) + 1
    for numero in numeros:
        soma += int(numero) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def gerar_cpf():
    """Gera um número de CPF válido."""
    # Gera os primeiros 9 dígitos aleatoriamente
    nove_digitos = [str(random.randint(0, 9)) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    dv1 = calcular_digito_verificador(nove_digitos)
    nove_digitos.append(str(dv1))

    # Calcula o segundo dígito verificador
    dv2 = calcular_digito_verificador(nove_digitos)
    
    cpf_gerado = "".join(nove_digitos) + str(dv2)
    return cpf_gerado

def formatar_cpf(cpf):
    """Formata o CPF no padrão XXX.XXX.XXX-XX."""
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido para formatação"
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

if __name__ == "__main__":
    cpf_novo = gerar_cpf()
    print(f"CPF Gerado (sem formatação): {cpf_novo}")
    print(f"CPF Gerado (formatado): {formatar_cpf(cpf_novo)}")
