# Web Scraping — Diário Oficial (Tabuleiros do Alto Parnaíba)

Este projeto automatiza a coleta de publicações do Diário Oficial dos Municípios do Piauí, focando no território **Tabuleiros do Alto Parnaíba**.

## 🎯 Escopo da Coleta
- **Ano:** 2025
- **Entidades:** Prefeitura e Câmara Municipal

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **Selenium**: Automação da navegação e interação com filtros.
- **Requests**: Download eficiente de arquivos.
- **UV**: Gerenciador de pacotes e ambiente virtual.

## ⚙️ Descrição da Implementação

A solução foi desenvolvida para lidar com a estrutura dinâmica do site da APPM (Scriptcase):
- **Navegação Dinâmica**: Gerenciamento de iframes e seleção automatizada de filtros.
- **Extração via Regex**: Captura de URLs de download embutidas em funções JavaScript.
- **Prevenção de Duplicidade**: O script verifica o histórico no CSV para evitar downloads repetidos.
- **Headless Mode**: Execução em segundo plano para otimização de recursos.

## 📂 Armazenamento de Dados

Os dados são salvos na pasta `dados_selenium/`:
- **CSV**: Contém metadados (edição, data, município, entidade, link e identificador único).
- **PDFs**: Organizados automaticamente em subpastas por `município/entidade`.
- **Relatório**: O arquivo `relatorio_geral.md` contém estatísticas detalhadas da coleta.

## 🚀 Guia de Execução

### Pré-requisitos
- Google Chrome ou Chromium instalado.
- [UV](https://github.com/astral-sh/uv) instalado no sistema.

### Comandos para Iniciar
```bash
# Acesse o diretório do projeto
cd webscraping-diario-oficial-tabuleiros-alto-parnaiba

# Sincronize as dependências e crie o ambiente virtual (.venv)
uv sync

# Execute o scraper
uv run python selenium_scraper.py
```

### 📊 Geração de Relatórios

Para gerar ou atualizar o relatório estatístico (Matriz de órgãos, evolução mensal e categorias), utilize:

```bash
uv run python gerar_relatorio.py
```
