import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df["Media Final"] = (df["Matematica"] + df["Portugues"] + df["Ciencias"]) /3
df.to_csv("notas_alunos_com_media.csv", index=False)

print(df[["Aluno", "Media Final"]])