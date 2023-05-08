import pandas as pd

planilha_dos_atletas = pd.read_csv("Atletas.csv")

apenas_atletas = planilha_dos_atletas.iloc[4: , 1:] # Linha x colunas;

modalidades_raw = planilha_dos_atletas.iloc[3, 1:]

modalidades = [modalidade for modalidade in modalidades_raw if str(type(modalidade)) == "<class 'str'>"]

myModalidades = open("./ATLETAS/MODALIDADES", "r").read().splitlines()

modal_to_myModal = {
    modalidades[i]: myModalidades[i] for i in range(24)
}

i = 0

atletas_list = []

for name in apenas_atletas:
    if i == 24:
        break
    for atletas in apenas_atletas[name]:
        if type(atletas) != str:
            if atletas_list:
                with open(f"./ATLETAS/{modal_to_myModal[modalidades[i]]}","w") as f:
                    print(modal_to_myModal[modalidades[i]])
                    for a in range(atletas_list.__len__()-1):
                        atl = (atletas_list[a]+"\n").upper().replace("AL ","")
                        f.write(atl)
                    atl = (atletas_list[atletas_list.__len__()-1]).upper().replace("AL ", "")
                    f.write(atl)
                i+=1
            atletas_list = []
            break
        else:
            if "SOMENTE" in atletas.upper() or "MASC" in atletas.upper() or "FEM" in atletas.upper() or "ATLETA" in atletas.upper():
                continue
            atletas_list.append(atletas)
        
