"""Validação de CPF (br).
Este módulo valida números de CPF brasileiros.
O CPF (Cadastro de Pessoas Físicas) é um número de identificação fiscal emitido pela Receita Federal do Brasil. Ele é composto por 11 dígitos, sendo os 9 primeiros o número base e os 2 últimos os dígitos verificadores.
"""

import re
from .generator import calculate_digit  # Importa a função de cálculo de dígito verificador do módulo generator

# Função para validar CPF
def validate_cpf(cpf: str) -> bool:
    """
    Valida um número de CPF brasileiro.

    A função primeiro limpa o CPF de entrada, removendo quaisquer caracteres
    não numéricos. Em seguida, verifica se o CPF limpo tem 11 dígitos
    e se não é uma sequência de dígitos repetidos (ex: "11111111111").
    Finalmente, calcula os dois dígitos verificadores com base nos primeiros
    nove dígitos e os compara com os dígitos fornecidos no CPF.

    Args:
        cpf: Uma string representando o número do CPF a ser validado.
             Pode conter ou não caracteres de formatação (pontos, traços).

    Returns:
        True se o CPF for válido, False caso contrário.
    """
    cpf_limpo = re.sub(r"[^0-9]", "", cpf)
    if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
        return False

    d1 = calculate_digit(cpf_limpo[:9])
    d2 = calculate_digit(cpf_limpo[:9] + d1)
    return cpf_limpo.endswith(d1 + d2)
