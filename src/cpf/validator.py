import re
# Supondo que generator.py está no mesmo diretório ou no PYTHONPATH
# Se estiverem no mesmo pacote, poderia ser: from .generator import ...
from generator import calcular_digito_verificador, formatar_cpf, gerar_cpf

def validar_cpf(cpf_a_validar: str) -> bool:
    """
    Valida um número de CPF.
    Verifica o formato, sequências inválidas e os dígitos verificadores.
    """
    if not isinstance(cpf_a_validar, str):
        return False

    # Remove caracteres não numéricos
    cpf_limpo = re.sub(r'[^0-9]', '', cpf_a_validar)

    # Verifica se tem 11 dígitos
    if len(cpf_limpo) != 11:
        return False

    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11), o que é inválido
    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    # Separa os números e os dígitos verificadores informados
    try:
        numeros_base = [int(digito) for digito in cpf_limpo[:9]]
        dv1_informado = int(cpf_limpo[9])
        dv2_informado = int(cpf_limpo[10])
    except ValueError:
        return False # Caso haja algum não-dígito que passou pelo regex (improvável)

    # Calcula o primeiro dígito verificador
    dv1_calculado = calcular_digito_verificador([str(d) for d in numeros_base])
    if dv1_calculado != dv1_informado:
        return False

    # Calcula o segundo dígito verificador
    numeros_com_dv1 = numeros_base + [dv1_calculado]
    dv2_calculado = calcular_digito_verificador([str(d) for d in numeros_com_dv1])
    if dv2_calculado != dv2_informado:
        return False

    return True

if __name__ == "__main__":
    print("--- Teste de Validação de CPF ---")

    # Teste com CPF gerado (que deve ser sempre válido)
    cpf_gerado_para_teste = gerar_cpf()
    print(f"\nTestando CPF gerado: {formatar_cpf(cpf_gerado_para_teste)}")
    if validar_cpf(cpf_gerado_para_teste):
        print(f"Resultado: O CPF {formatar_cpf(cpf_gerado_para_teste)} é VÁLIDO (Esperado: VÁLIDO) - CORRETO")
    else:
        print(f"Resultado: O CPF {formatar_cpf(cpf_gerado_para_teste)} é INVÁLIDO (Esperado: VÁLIDO) - INCORRETO")

    # Testes com CPFs conhecidos
    cpfs_para_testar = [
        ("111.111.111-11", False, "Todos os dígitos iguais"),
        ("123.456.789-00", False, "Dígitos verificadores incorretos"),
        ("00000000000", False, "Todos os dígitos iguais (sem formatação)"),
        ("12345", False, "Comprimento incorreto"),
        ("abcdefghijk", False, "Não numérico"),
        (gerar_cpf(), True, "CPF válido gerado dinamicamente"), # Testa outro CPF gerado
        ("53476490097", True, "CPF válido conhecido"), # Exemplo de CPF válido
        ("53476490098", False, "CPF inválido conhecido (DV2 errado)"), # Exemplo de CPF inválido
    ]

    for cpf_str, esperado, descricao in cpfs_para_testar:
        resultado = validar_cpf(cpf_str)
        status_resultado = "VÁLIDO" if resultado else "INVÁLIDO"
        status_esperado = "VÁLIDO" if esperado else "INVÁLIDO"
        verificacao = "CORRETO" if resultado == esperado else "INCORRETO"
        print(f"\nTestando CPF: {cpf_str} ({descricao})")
        print(f"Resultado: {status_resultado} (Esperado: {status_esperado}) - {verificacao}")