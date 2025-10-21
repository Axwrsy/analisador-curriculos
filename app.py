import os
import pandas as pd
from pdfminer.high_level import extract_text

# === palavras chaves com base nas vagas de back-end===
PALAVRAS_CHAVE = ["Java", "Python", "JavaScript", "TypeScript", "SQL", "NoSQL", "Git", "API RESTful", "Programação Orientada a Objetos", "Desenvolvimento Ágil", "Scrum", "Kanban", ".NET", "C#", "Node.js", "Spring Boot", "Django", "PostgreSQL", "MySQL", "Oracle", "AWS", "Cloud"]

# === caminho da pasta com os currículos ===
PASTA_CURRICULOS = "curriculos"

# === função para pontuar cada currículo ===
def analisar_curriculo(caminho_pdf):
    texto = extract_text(caminho_pdf)
    texto = texto.lower()
    
    pontuacao = sum(1 for palavra in PALAVRAS_CHAVE if palavra.lower() in texto)
    return pontuacao, texto

# === loop pelos PDFs ===
resultados = []

for arquivo in os.listdir(PASTA_CURRICULOS):
    if arquivo.lower().endswith(".pdf"):
        caminho = os.path.join(PASTA_CURRICULOS, arquivo)
        pontuacao, _ = analisar_curriculo(caminho)
        resultados.append({"Arquivo": arquivo, "Pontuação": pontuacao})

# === verifica se encontrou currículos ===
if not resultados:
    print(" Nenhum arquivo PDF encontrado na pasta 'curriculos/'.")
else:
    # === gera relatório final ===
    df = pd.DataFrame(resultados).sort_values(by="Pontuação", ascending=False)
    print(df)

    # ===slva em xls ===
    df.to_excel("resultado_curriculos.xlsx", index=False)
    print("\n Relatório salvo como resultado_curriculos.xlsx")
