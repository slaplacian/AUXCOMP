efetivo = open("../Efetivo3ano","r").read().splitlines()

atletas = open("Atletas", "r").read().splitlines()

nao_atletas = []

for aluno in efetivo:
    if aluno not in atletas:
        nao_atletas.append(aluno)

with open("NãoAtletas","w") as f:
    for aluno in nao_atletas:
        f.write(aluno+"\n")