# analisador de currículos

projeto em python que lê arquivos pdf de currículos, identifica palavras-chave e gera uma pontuação automática para cada candidato, com base nas habilidades encontradas no texto.

---

## objetivo

o objetivo é facilitar a triagem de currículos, analisando de forma simples quais candidatos possuem as competências mais relevantes para uma vaga específica.

---

##  funcionamento

o programa:
1. lê todos os arquivos `.pdf` dentro da pasta `curriculos/`
2. extrai o texto de cada currículo
3. verifica a presença das palavras-chave definidas no início do código
4. soma uma pontuação baseada nas habilidades encontradas
5. gera um relatório final em excel com o ranking dos currículos

---

##  exemplo de palavras-chave

```python
palavras_chave = ["python", "excel", "análise de dados", "sql", "flask", "gestão"]


requisitos - instalar:

pip install -r requisitos.txt


pip install pdfminer.six pandas openpyxl
