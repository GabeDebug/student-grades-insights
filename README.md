## 📊 Calculadora de Média de Alunos

Este é um projeto simples de **Data Science** (ou análise de dados) implementado em Python que calcula a **Média Final** das notas dos alunos a partir de um arquivo CSV de entrada e salva o resultado em um novo arquivo.

-----

### 🚀 Começando

Estas instruções ajudarão você a colocar o projeto em funcionamento em sua máquina local para fins de desenvolvimento e teste.

#### 📋 Pré-requisitos

Você precisará ter o **Python** instalado em sua máquina. O script utiliza a biblioteca **Pandas** para manipulação de dados.

Instale a biblioteca `pandas` usando `pip`:

```bash
pip install pandas
```

#### 📁 Estrutura do Projeto

O projeto é composto por dois arquivos principais:

1.  **`calcular_media.py`**: O script Python que realiza o cálculo.
2.  **`notas_alunos.csv`**: O arquivo de dados de entrada que contém as notas dos alunos. **Este arquivo deve ser criado por você** seguindo o formato especificado abaixo.

-----

### 📝 Uso

#### 1\. Arquivo de Entrada (`notas_alunos.csv`)

O script espera um arquivo CSV chamado **`notas_alunos.csv`** no mesmo diretório que o script `calcular_media.py`. Este arquivo deve ter a seguinte estrutura (com cabeçalhos exatos):

| Aluno | Matematica | Portugues | Ciencias |
| :---: | :--------: | :-------: | :------: |
| Maria | 8.0 | 7.5 | 9.0 |
| João | 6.5 | 8.0 | 7.0 |
| ... | ... | ... | ... |

**Exemplo de Conteúdo (`notas_alunos.csv`):**

```csv
Aluno,Matematica,Portugues,Ciencias
Maria,8.0,7.5,9.0
João,6.5,8.0,7.0
Ana,9.0,9.0,8.5
Pedro,5.5,6.0,7.5
```

#### 2\. Executando o Script

Execute o script Python a partir do seu terminal:

```bash
python calcular_media.py
```

#### 3\. Saída

Após a execução, duas coisas acontecerão:

  * **Impressão no Terminal**: O script exibirá o nome do aluno e a **Média Final** calculada no terminal.

    ```
         Aluno  Media Final
    0    Maria     8.166667
    1     João     7.166667
    2      Ana     8.833333
    3    Pedro     6.333333
    ```

  * **Novo Arquivo CSV**: Um novo arquivo chamado **`notas_alunos_com_media.csv`** será criado no mesmo diretório. Este arquivo conterá todas as colunas do original mais a nova coluna **"Media Final"**.

    **Exemplo de Conteúdo (`notas_alunos_com_media.csv`):**

    ```csv
    Aluno,Matematica,Portugues,Ciencias,Media Final
    Maria,8.0,7.5,9.0,8.166666666666666
    João,6.5,8.0,7.0,7.166666666666667
    Ana,9.0,9.0,8.5,8.833333333333334
    Pedro,5.5,6.0,7.5,6.333333333333333
    ```

-----

### ⚙️ Como Funciona o Código (`calcular_media.py`)

```python
import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df["Media Final"] = (df["Matematica"] + df["Portugues"] + df["Ciencias"]) /3
df.to_csv("notas_alunos_com_media.csv", index=False)

print(df[["Aluno", "Media Final"]])
```

O script segue as seguintes etapas:

1.  **Importa** a biblioteca `pandas`.
2.  **Lê** o arquivo CSV de entrada (`notas_alunos.csv`) em um DataFrame.
3.  **Calcula** a **"Media Final"** somando as notas das colunas **"Matematica"**, **"Portugues"**, e **"Ciencias"** e dividindo por 3.
4.  **Salva** o DataFrame modificado no novo arquivo CSV (`notas_alunos_com_media.csv`).
5.  **Imprime** as colunas "Aluno" e "Media Final" no terminal.

-----

### 🤝 Contribuições

Sinta-se à vontade para sugerir melhorias, como:

  * Adicionar tratamento de erros para arquivos ausentes.
  * Calcular outras estatísticas (desvio padrão, nota máxima/mínima).
  * Permitir que as disciplinas e pesos sejam configuráveis.

-----

### 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE.md` para detalhes.