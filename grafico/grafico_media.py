import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("notas_alunos_com_media.csv")

plt.figure(figsize=(10,6))
plt.bar(df["Aluno"], df["Media Final"])
plt.xlabel("Aluno")
plt.ylabel("Média Final")
plt.title("Média Final dos Alunos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("media_final_grafico.png")   
plt.show()                               
