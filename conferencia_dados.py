#ferramenta para trabalhar dados
import pandas as pd
import tabula
from tabula import read_pdf

#convertendo pdf em csv
tabula.convert_into("dados\sistema .pdf", "dados\sistema.csv", output_format = "csv", pages = "all")
sistema = tabula.read_pdf("dados\sistema .pdf", pages = "all")

#convertendo arquivo excel em csv
drive = pd.read_excel("dados/drive.xlsx")
print(type(drive))
#tabela com as diferenças entre as bases de dados
diff = pd.merge("dados\sistema.csv",drive, on = "RG, NOME, CONVENIO, VALOR", how = "outer")
conferencia = diff.loc[lambda x: x["merge"] != "both"]
print(conferencia)