"""
Interface de Linha de Comando (CLI) para Geração e Validação de CPFs.

Este script fornece uma interface de linha de comando para interagir com as
funcionalidades de geração e validação de CPFs implementadas nos módulos
`cpf.generator` e `cpf.validator`.

Permite ao usuário:
- Gerar um novo número de CPF válido, com ou sem formatação.
- Validar um número de CPF existente.

Uso:
  python cli.py generate [--raw]
  python cli.py validate <CPF_NUMBER>
  python cli.py --help
"""

import argparse  # Adicionado para análise de argumentos
import sys  # Adicionado para tratamento de erros
import re  # Adicionado para formatação opcional na saída

# Importa as funções de geração e validação de CPF
from cpf.generator import generate_cpf
from cpf.validator import validate_cpf


def main():
    """
    Função principal para executar a interface de linha de comando.

    Configura o `ArgumentParser` para lidar com os subcomandos 'generate' e 'validate'.
    - O subcomando 'generate' pode aceitar um argumento opcional '--raw' para
      controlar a formatação do CPF gerado.
    - O subcomando 'validate' requer um argumento posicional 'cpf' que é o
      número do CPF a ser validado.

    Com base no subcomando e nos argumentos fornecidos, chama as funções
    apropriadas de `generate_cpf` ou `validate_cpf` e imprime o resultado.
    Se nenhum subcomando for fornecido ou se um subcomando inválido for usado,
    a mensagem de ajuda é exibida e o script termina com um código de erro.
    """
    # Configuração do ArgumentParser
    parser = argparse.ArgumentParser(description="Gerador e validador de CPF - CLI.")
    subparsers = parser.add_subparsers(
        dest="command", help="Comandos disponíveis", required=True
    )  # Adicionado help e required

    # Subcomando para gerar CPF
    generate_parser = subparsers.add_parser("generate", help="Gerar um CPF válido:")
    generate_parser.add_argument(
        "--raw",
        action="store_true",
        help="Gerar CPF sem formatação (apenas os 11 dígitos).",  # Melhorada a descrição
    )

    # Subcomando para validar CPF
    validate_parser = subparsers.add_parser("validate", help="Validar um CPF.")

    validate_parser.add_argument(
        "cpf",
        type=str,
        help="O número do CPF a ser validado (pode estar formatado ou não).",  # Melhorada a descrição
    )

    args = parser.parse_args()

    # Verifica o comando e executa a ação correspondente
    if args.command == "generate":
        cpf_gerado = generate_cpf(formatted=not args.raw)  # Renomeado para clareza
        print(f"CPF gerado: {cpf_gerado}")
    elif args.command == "validate":
        is_valid = validate_cpf(args.cpf)
        # Formata o CPF de entrada para exibição, se possível, para consistência
        # Isso é opcional e depende se você quer sempre mostrar o CPF formatado na saída
        cpf_display = args.cpf
        try:
            # Tenta formatar se for um CPF válido em termos de dígitos, mesmo que os DVs não batam
            # Isso é apenas para exibição, a validação já foi feita
            cpf_numeros_input = re.sub(r"[^0-9]", "", args.cpf)
            if len(cpf_numeros_input) == 11:
                cpf_display = f"{cpf_numeros_input[:3]}.{cpf_numeros_input[3:6]}.{cpf_numeros_input[6:9]}-{cpf_numeros_input[9:]}"
        except Exception:
            pass  # Mantém o original se a formatação falhar

        # Exibe o resultado da validação
        # O CPF pode estar formatado ou não, mas a validação deve ser feita com o CPF limpo
        if is_valid:
            print(f"O CPF {cpf_display} é válido.")
        # Caso o CPF não seja válido, exibe uma mensagem apropriada
        else:
            print(f"O CPF {cpf_display} é inválido.")
    # O bloco else não é mais necessário se 'required=True' for usado em subparsers,
    # pois o argparse lidará com a ausência de comando.


if __name__ == "__main__":
    main()
