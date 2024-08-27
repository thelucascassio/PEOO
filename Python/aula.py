#2. Ler nome e matrícula de 10 alunos, mostrar nome, matrícula e ano de ingresso no IFRN de cada aluno
n = []
m = []
for i in range(3):
    nome = input("Informe seu nome: ")
    matr = input("Informe sua matrícula")
    n.append(nome)
    m.append(matr)

for i in range(3):
    matr = m[i]
    ano = int(matr[0:4]) #ano = int(m[k][0:4])
    print(f"Nome = {n[i]} - Matrícula: = {m[i]} - Ano = {ano}")