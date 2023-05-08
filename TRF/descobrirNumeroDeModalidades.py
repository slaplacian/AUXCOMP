atletas = open("Atletas","r").read().splitlines()

nums = []

for atleta in atletas:
    with open("./MODALIDADES/"+atleta, "r") as f:
        num = f.read().splitlines().__len__()
        nums.append(num)

with open("./AtletasCNumModalidades", "w") as f:
    for i in range(atletas.__len__()):
        f.write(atletas[i]+" "+str(nums[i])+"\n")