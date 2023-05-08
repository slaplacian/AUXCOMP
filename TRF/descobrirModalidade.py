atletas = open("./Atletas").read().splitlines()

modalidades = open("./ATLETAS/MODALIDADES").read().splitlines()

for atleta in atletas:
    modalidades_desse_atleta = []
    for modalidade in modalidades:
        with open("./ATLETAS/"+modalidade) as f:
            atl_nessa_modalidade = f.read().splitlines()
            for atl in atl_nessa_modalidade:
                j1 = 'JULIANA' == atleta and atl == 'JULIANA LIMA'
                if atleta in atl and not j1:
                    modalidades_desse_atleta.append(modalidade)
    with open("./MODALIDADES/"+atleta,"w") as f:
        for modalidade in modalidades_desse_atleta:
            f.write(modalidade+"\n")