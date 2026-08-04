# Relatório de Estatística Aplicada

Este repositório contém o relatório desenvolvido para a disciplina de **Estatística Aplicada**, bem como os códigos em Python utilizados durante a análise dos dados.

## Requisitos

* Python 3.10 ou superior
* Quarto
* Uma distribuição LaTeX (TinyTeX, TeX Live ou equivalente)

## Como executar

1. Entre na pasta do relatório:

```bash
cd Relatorio
```

2. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

3. Renderize o relatório em PDF:

```bash
quarto render relatorio.qmd --to modeloufcg-pdf
```

O arquivo PDF gerado será salvo na própria pasta do relatório.

## Material complementar

Além do relatório final, este repositório também contém os códigos em Python desenvolvidos ao longo da elaboração do artigo. Esses arquivos servem como material complementar e de apoio, permitindo acompanhar todas as etapas da análise estatística, incluindo:

* Análise exploratória dos dados;
* Construção e seleção de modelos de regressão;
* Diagnóstico dos pressupostos;
* Identificação de observações influentes;
* Geração de tabelas e gráficos utilizados no relatório.
