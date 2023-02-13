#ferramenta para trabalhar dados
import pandas as pd
import tabula
from tabula import read_pdf

#convertendo pdf em csv
tabula.convert_into("arquivos\sistema.pdf", "arquivos\sistema.csv", output_format = "csv", pages = "all")
sistema = tabula.read_pdf("arquivos\sistema.pdf", pages = "all")
print(type(sistema))
#convertendo arquivo excel em csv
drive = pd.read_excel("arquivos/drive.xlsx")
print(type(drive))
#tabela com as diferenças entre as bases de dados
diff = pd.merge("arquivos\sistema.csv",drive, on = "RG, NOME, CONVENIO, VALOR", how = "outer")
conferencia = diff.loc[lambda x: x["meege"] != "both"]
print(conferencia)

