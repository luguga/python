import pandas as pd
import os
import glob

#diretorio onde estão os arquivos novos
my_dir_in = os.fspath('D:\Downloads\FilesIn')

#diretorio do arquivo de base
my_dir_out = os.fspath("D:\Downloads\FilesOut") + "\\base.txt"

#captura data do arquivo de saída, para empilhar só as novidades
data_ref = os.path.getmtime(my_dir_out)

#carrega o arquivo destino na memória
df = pd.DataFrame(pd.read_csv(my_dir_out))

#captura arquivo a arquivo do diretorio origem
for files in glob.glob(my_dir_in + "\\" + "*.txt"):

#check se a data do arquivo é maior que a base (somente arquivos novos)

    if os.path.getmtime(files)>=data_ref:
# carrega o arquivo novo

        frame = pd.read_csv(files)
#atualiza o arquivo da memória

        df = df.append(frame)

#ao finalizar as leituras, salva o arquivo novo
df.to_csv(my_dir_out,index=False)