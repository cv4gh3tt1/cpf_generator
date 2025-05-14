import random


# Função para calcular o dígito verificador do CPF
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
    if not digits.isdigit():
        raise ValueError("Todos os caracteres em 'digits' devem ser numéricos.")

    total = sum((len(digits) + 1 - i) * int(n) for i, n in enumerate(digits))
    remainder = 11 - (total % 11)
    return "0" if remainder > 9 else str(remainder)


# Função para gerar um CPF válido
def generate_cpf(formatted: bool = True) -> str:
    """
    Gera um número de CPF (Cadastro de Pessoas Físicas) brasileiro válido.

    A função primeiro gera 9 dígitos aleatórios que formam a base do CPF.
    Em seguida, calcula os dois dígitos verificadores (DV) com base nesses
    9 dígitos, seguindo o algoritmo da Receita Federal Brasileira.

    Args:
        formatted: Um booleano que indica se o CPF gerado deve ser
                   retornado com formatação (XXX.XXX.XXX-XX) ou
                   apenas os 11 dígitos. O padrão é True (formatado).

    Returns:
        Uma string contendo o número de CPF válido, formatado ou não,
        conforme especificado pelo parâmetro `formatted`.
    """

    base = "".join([str(random.randint(0, 9)) for _ in range(9)])
    d1 = calculate_digit(base)
    d2 = calculate_digit(base + d1)
    cpf = base + d1 + d2

    if formatted:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf
