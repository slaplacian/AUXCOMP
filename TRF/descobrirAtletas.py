modalidades = open("./ATLETAS/MODALIDADES").read().splitlines()

todos_os_atletas = []

ATLETAS = open("Atletas", "w")

for modalidade in modalidades:
    with open("./ATLETAS/"+modalidade) as f:
        atletas_por_modalidade = f.read().splitlines()
        novos_atl = []
        for atleta in atletas_por_modalidade:
            if "(" in atleta:
                novos_atl = atleta.split(" (")
        if novos_atl:
            atletas_por_modalidade.remove(novos_atl[0]+" ("+novos_atl[1])
            atletas_por_modalidade.append(novos_atl[0])
            atletas_por_modalidade.append(novos_atl[1][:-1])
        
        for atleta in atletas_por_modalidade:
            todos_os_atletas.append(atleta)

set_atl_sem_rep = set(todos_os_atletas)

atl_sem_rep = tuple(set_atl_sem_rep)

atl_sem_rep = list(atl_sem_rep)

atl_sem_rep.sort()

for atletas in atl_sem_rep:
    ATLETAS.write(atletas+"\n")