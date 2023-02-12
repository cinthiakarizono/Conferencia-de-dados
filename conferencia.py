#ferramenta para trabalhar dados
import pandas as pd
#converte arquivos pdf em csv
import tabula
sistema = tabula.read_pdf("arquivos/sistema.pdf", pages = "all")
print(sistema)
read = pd.read_excel("arquivos/drive.xlsx")
read.to_csv("arquivos/drive.csv", index = None, header = True)

