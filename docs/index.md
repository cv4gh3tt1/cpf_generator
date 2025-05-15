# CPF Generator/Validator

Projeto para geração e validação de números de CPF (Cadastro de Pessoas Físicas) brasileiros via linha de comando ou como biblioteca Python.

---

## Funcionalidades

- **Gerar CPF válido:** Gera números de CPF válidos, com ou sem formatação.
- **Validar CPF:** Verifica se um número de CPF informado é válido, aceitando formatos com ou sem pontuação.
- **Interface de Linha de Comando (CLI):** Permite gerar e validar CPFs diretamente pelo terminal.
- **Módulos reutilizáveis:** Funções de geração e validação podem ser usadas em outros projetos Python.

---

## Instalação

Clone o repositório e instale as dependências (recomenda-se uso de ambiente virtual):

```sh
git clone https://github.com/cv4gh3tt1/cpf_generator.git
cd cpf_generator
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

---

## Uso

### Como CLI

- **Gerar CPF formatado:**
  ```sh
  python src/cli.py generate
  ```
- **Gerar CPF sem formatação:**
  ```sh
  python src/cli.py generate --raw
  ```
- **Validar um CPF:**
  ```sh
  python src/cli.py validate 123.456.789-09
  ```

### Como biblioteca Python

```python
from cpf.generator import generate_cpf
from cpf.validator import validate_cpf

cpf = generate_cpf()  # Gera CPF formatado
print(cpf)

print(validate_cpf(cpf))  # True
```

---

## Estrutura do Projeto

```
cpf_generator/
├── src/
│   ├── cli.py                # Interface de linha de comando
│   └── cpf/
│       ├── __init__.py
│       ├── generator.py      # Função para gerar CPF
│       └── validator.py      # Função para validar CPF
├── tests/                    # Testes automatizados
│   ├── test_generator.py
│   └── test_validator.py
├── docs/                     # Documentação do projeto
│   └── index.md
├── requirements.txt          # Dependências do projeto
├── mkdocs.yml                # Configuração da documentação
└── .gitignore
```

---

## Outras Informações Relevantes

- **Documentação online:** Consulte a documentação em [docs/index.md](https://github.com/cv4gh3tt1/cpf_generator/blob/main/docs/index.md)
- **Testes:** Os arquivos de teste estão em [tests/](tests/).
- **Licença:** Consulte o repositório para informações de licença.
- **Contribuição:** Pull requests são bem-vindos!

---

Dúvidas ou sugestões? Abra uma issue no [repositório do projeto](https://github.com/cv4gh3tt1/cpf_generator).