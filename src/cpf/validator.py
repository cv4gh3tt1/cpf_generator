"""Validação de CPF (br).
Este módulo valida números de CPF brasileiros.
O CPF (Cadastro de Pessoas Físicas) é um número de identificação fiscal emitido pela Receita Federal do Brasil. Ele é composto por 11 dígitos, sendo os 9 primeiros o número base e os 2 últimos os dígitos verificadores.
"""

import re


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

    def calculate_digit(digits: str) -> str:
        """
        Calcula um dígito verificador do CPF com base nos dígitos fornecidos.

        O cálculo é feito multiplicando cada dígito por um peso decrescente
        (começando em len(digits) + 1), somando os resultados, e então
        calculando o resto da divisão por 11. O dígito verificador é
        11 menos esse resto, a menos que o resultado seja 10 ou 11,
        caso em que o dígito verificador é 0.

        Args:
            digits: Uma string contendo os dígitos base para o cálculo
                    (9 dígitos para o primeiro DV, 10 para o segundo DV).

        Returns:
            Uma string representando o dígito verificador calculado ("0" a "9").
        """
        total = sum((len(digits) + 1 - i) * int(n) for i, n in enumerate(digits))
        remainder = 11 - (total % 11)
        return "0" if remainder > 9 else str(remainder)

    d1 = calculate_digit(cpf_limpo[:9])
    d2 = calculate_digit(cpf_limpo[:9] + d1)
    return cpf_limpo.endswith(d1 + d2)