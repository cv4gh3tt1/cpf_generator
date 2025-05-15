# Documentação do Projeto CPF Generator/Validator

Bem-vindo à documentação do projeto CPF Generator/Validator. Este projeto oferece funcionalidades para gerar e validar números de CPF (Cadastro de Pessoas Físicas) brasileiros.

## Funcionalidades

O projeto é composto por dois módulos principais:

*   `generator.py`: Contém a lógica para gerar um número de CPF válido.
*   `validator.py`: Contém a lógica para validar se um determinado número de CPF é válido.

## Como Usar

Assumindo que você tem os arquivos `generator.py` e `validator.py` no seu caminho Python, você pode importar e usar as funções diretamente:

```python
# Exemplo de uso do gerador
from generator import generate_cpf

novo_cpf = generate_cpf()
print(f"CPF Gerado: {novo_cpf}")

# Exemplo de uso do validador
from validator import validate_cpf

cpf_para_validar = "123.456.789-00" # Substitua por um CPF real para testar
if validate_cpf(cpf_para_validar):
    print(f"O CPF {cpf_para_validar} é válido.")
else:
    print(f"O CPF {cpf_para_validar} é inválido.")

# Exemplo validando o CPF gerado
if validate_cpf(novo_cpf):
    print(f"O CPF gerado ({novo_cpf}) é válido.")
else:
    print(f"O CPF gerado ({novo_cpf}) é inválido.")
```

Certifique-se de que os arquivos `generator.py` e `validator.py` estejam acessíveis (por exemplo, na mesma pasta do script que os importa ou instalados como um pacote).

Para mais detalhes sobre a implementação, consulte o código-fonte dos respectivos arquivos.
