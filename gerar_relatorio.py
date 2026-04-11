import csv
import os
from collections import Counter, defaultdict
from datetime import datetime

PATH_CSV = "dados_selenium/csv/dados_coletados.csv"
PATH_RELATORIO = "dados_selenium/relatorio_geral.md"

def gerar():
    if not os.path.exists(PATH_CSV):
        print(f"[!] Arquivo {PATH_CSV} não encontrado.")
        return

    with open(PATH_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter="|")
        dados = list(reader)

    total_registros = len(dados)
    
    # Contadores e Agrupamentos
    municipios = Counter()
    categorias = Counter()
    distribuicao_mensal = Counter()
    matriz_mun_ent = defaultdict(lambda: Counter())
    
    datas = []
    
    for d in dados:
        m = d['Município']
        e = d['Entidade']
        c = d['Categoria']
        data_str = d['Data']
        
        municipios[m] += 1
        categorias[c] += 1
        matriz_mun_ent[m][e] += 1
        
        try:
            dt = datetime.strptime(data_str, "%d/%m/%Y")
            datas.append(dt)
            # Formato YYYY-MM para ordenação fácil
            mes_chave = dt.strftime("%Y-%m")
            mes_nome = dt.strftime("%B")
            distribuicao_mensal[f"{mes_chave} ({mes_nome})"] += 1
        except:
            pass

    # Metadados de Tempo
    periodo_inicio = min(datas).strftime("%d/%m/%Y") if datas else "N/A"
    periodo_fim = max(datas).strftime("%d/%m/%Y") if datas else "N/A"

    relatorio = [
        "# 📊 Relatório Detalhado de Coleta — 2025",
        f"\n> **Território:** Tabuleiros do Alto Parnaíba",
        f"> **Total de Registros:** {total_registros}",
        f"> **Período Coberto:** {periodo_inicio} até {periodo_fim}",
        
        "\n## 📍 Matriz Município vs Entidade",
        "Detalhamento de quantos registros foram encontrados em cada órgão.",
        "\n| Município | Prefeitura | Câmara | **Total** |",
        "| :--- | :---: | :---: | :---: |"
    ]

    for m in sorted(municipios.keys()):
        pref = matriz_mun_ent[m]['Prefeitura']
        cam = matriz_mun_ent[m]['Camara']
        total = pref + cam
        relatorio.append(f"| {m} | {pref} | {cam} | **{total}** |")

    relatorio.extend([
        "\n## 📅 Evolução Mensal",
        "Quantidade de publicações detectadas por mês.",
        "\n| Mês | Publicações | % |",
        "| :--- | :---: | :---: |"
    ])
    
    for mes in sorted(distribuicao_mensal.keys()):
        count = distribuicao_mensal[mes]
        pct = (count / total_registros) * 100
        relatorio.append(f"| {mes} | {count} | {pct:.1f}% |")

    relatorio.extend([
        "\n## 📂 Classificação por Categoria (Top 15)",
        "\n| Categoria | Total | % |",
        "| :--- | :---: | :---: |"
    ])
    for c, count in categorias.most_common(15):
        pct = (count / total_registros) * 100
        relatorio.append(f"| {c} | {count} | {pct:.1f}% |")

    relatorio.append(f"\n\n---\n*Relatório gerado automaticamente em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")

    with open(PATH_RELATORIO, 'w', encoding='utf-8') as f:
        f.write("\n".join(relatorio))

    print(f"[*] Relatório detalhado gerado: {PATH_RELATORIO}")

if __name__ == "__main__":
    gerar()
